#!/usr/bin/env python3
"""
Reddit search via Composio.

Uses Composio's Reddit toolkit to search Reddit without direct API keys.
"""

import os
import json
from typing import Optional
from datetime import datetime, timezone


def get_composio_api_key() -> str:
    """Get Composio API key from environment."""
    key = os.environ.get("COMPOSIO_API_KEY")
    if not key:
        raise ValueError("COMPOSIO_API_KEY not set. Set COMPOSIO_API_KEY in your shell or ~/.openclaw/.env")
    return key


def get_user_id() -> str:
    """Get Composio User ID from environment (formerly entity_id)."""
    return os.environ.get("COMPOSIO_USER_ID", "pg-test-YOUR-USER-ID")


def get_connection_id() -> Optional[str]:
    """Get optional Reddit connection ID."""
    return os.environ.get("COMPOSIO_REDDIT_CONNECTION_ID")


def search_reddit(
    api_key: str,
    user_id: str,
    query: str,
    max_results: int = 10,
    connection_id: Optional[str] = None,
) -> dict:
    """
    Search Reddit via Composio.
    
    Args:
        api_key: Composio API key
        user_id: Composio User ID
        query: Search query
        max_results: Maximum number of results
        connection_id: Optional Reddit connection ID
    
    Returns:
        Composio API response
    """
    import httpx
    
    base_url = "https://backend.composio.dev/api"
    
    # Build request body for Reddit search
    body = {
        "userId": user_id,
        "input": {
            "query": query,
            "limit": max_results,
        },
    }
    
    if connection_id:
        body["connectedAccountId"] = connection_id
    
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json",
    }
    
    # Use Reddit search tool via Composio v2 API
    with httpx.Client(timeout=60.0) as client:
        response = client.post(
            f"{base_url}/v2/actions/REDDIT_REDDIT_SEARCH/execute",
            headers=headers,
            json=body,
        )
        
        if not response.ok:
            error_text = response.text[:500]
            raise Exception(f"Composio {response.status_code}: {error_text}")
        
        result = response.json()
        
        if not result.get("success") and result.get("error"):
            raise Exception(f"Composio error: {result.get('error')}")
        
        return result.get("data", {})


def parse_reddit_response(response: dict) -> list:
    """
    Parse Composio Reddit response into standardized format.
    
    Args:
        response: Composio API response
    
    Returns:
        List of parsed Reddit posts
    """
    posts = []
    
    # Handle different response structures
    data = response.get("data", response)
    items = data if isinstance(data, list) else data.get("data", [])
    
    for item in items:
        # Normalize different Reddit API response formats
        if "title" in item:
            # Direct Reddit API format
            posts.append({
                "title": item.get("title", ""),
                "url": item.get("url", f"https://reddit.com{item.get('permalink', '')}"),
                "score": item.get("score", 0),
                "num_comments": item.get("num_comments", 0),
                "author": item.get("author", ""),
                "subreddit": item.get("subreddit", ""),
                "created_utc": item.get("created_utc", 0),
                "selftext": item.get("selftext", ""),
            })
        elif "text" in item:
            # X-style format
            posts.append({
                "title": item.get("text", "")[:200],
                "url": item.get("url", ""),
                "score": item.get("metrics", {}).get("likes", 0),
                "num_comments": item.get("metrics", {}).get("replies", 0),
                "author": item.get("username", item.get("author", "")),
                "subreddit": item.get("subreddit", ""),
                "created_utc": item.get("created_at", item.get("created_utc", "")),
                "selftext": "",
            })
    
    return posts


def enrich_with_metrics(posts: list) -> list:
    """
    Add engagement metrics to posts.
    
    Args:
        posts: List of parsed posts
    
    Returns:
        Posts with engagement data
    """
    enriched = []
    for post in posts:
        # Calculate engagement score
        score = post.get("score", 0)
        comments = post.get("num_comments", 0)
        engagement = score + (comments * 2)  # Weight comments
        
        post["engagement"] = engagement
        enriched.append(post)
    
    return enriched


def search_reddit_topic(
    query: str,
    max_results: int = 20,
    api_key: Optional[str] = None,
    user_id: Optional[str] = None,
    connection_id: Optional[str] = None,
    from_date: Optional[str] = None,
    to_date: Optional[str] = None,
) -> list:
    """
    Search Reddit for a topic.
    
    Args:
        query: Search query
        max_results: Maximum results
        api_key: Composio API key (uses env if not provided)
        user_id: Composio User ID (uses env if not provided)
        connection_id: Optional Reddit connection ID
        from_date: Optional start date (not fully implemented)
        to_date: Optional end date (not fully implemented)
    
    Returns:
        List of parsed Reddit posts with metrics
    """
    if not api_key:
        api_key = get_composio_api_key()
    if not user_id:
        user_id = get_user_id()
    
    response = search_reddit(
        api_key=api_key,
        user_id=user_id,
        query=query,
        max_results=max_results,
        connection_id=connection_id,
    )
    
    posts = parse_reddit_response(response)
    posts = enrich_with_metrics(posts)
    
    return posts


if __name__ == "__main__":
    import sys
    
    # Simple test
    api_key = get_composio_api_key()
    user_id = get_user_id()
    conn_id = get_connection_id()
    
    query = sys.argv[1] if len(sys.argv) > 1 else "AI"
    results = search_reddit_topic(query, api_key=api_key, user_id=user_id, connection_id=conn_id)
    
    print(f"Found {len(results)} posts:")
    for post in results[:5]:
        print(f"  - {post['title'][:80]}... ({post.get('engagement', 0)} engagement)")

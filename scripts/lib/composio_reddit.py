#!/usr/bin/env python3
"""
Reddit search via Composio.

Uses Composio's Reddit toolkit to search Reddit without direct API keys.
Composio v3 uses userId instead of entityId/connectionId.
"""

import os
import json
from typing import Optional


def get_composio_api_key() -> str:
    """Get Composio API key from environment."""
    key = os.environ.get("COMPOSIO_API_KEY")
    if not key:
        raise ValueError("COMPOSIO_API_KEY not set. Set COMPOSIO_API_KEY in your shell or ~/.openclaw/.env")
    return key


def get_entity_id() -> str:
    """Get Composio Entity/User ID from environment."""
    return os.environ.get("COMPOSIO_USER_ID", "pg-test-YOUR-USER-ID")


def search_reddit(
    api_key: str,
    entity_id: str,
    query: str,
    max_results: int = 10,
) -> dict:
    """
    Search Reddit via Composio.

    Composio v3 uses entityId instead of userId or connectionId.
    No connected account needed - Composio manages authenticated sessions.

    Args:
        api_key: Composio API key
        entity_id: Composio User/Entity ID
        query: Search query
        max_results: Maximum number of results

    Returns:
        Composio API response
    """
    import httpx

    base_url = "https://backend.composio.dev/api"

    body = {
        "appName": "REDDIT",
        "entityId": entity_id,
        "input": {
            "query": query,
            "limit": max_results,
        },
    }

    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json",
    }

    with httpx.Client(timeout=60.0) as client:
        response = client.post(
            f"{base_url}/v2/actions/REDDIT_REDDIT_SEARCH/execute",
            headers=headers,
            json=body,
        )

        # Composio returns JSON directly
        result = response.json()

        if not result.get("success") and result.get("error"):
            raise Exception(f"Composio error: {result.get('error')}")

        return result.get("data", {})


def parse_reddit_response(response: dict) -> list:
    """Parse Composio Reddit response into standardized format."""
    posts = []

    data = response.get("data", response)
    items = data if isinstance(data, list) else data.get("data", [])

    for item in items:
        if "title" in item:
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
    """Add engagement metrics to posts."""
    enriched = []
    for post in posts:
        score = post.get("score", 0)
        comments = post.get("num_comments", 0)
        engagement = score + (comments * 2)
        post["engagement"] = engagement
        enriched.append(post)
    return enriched


def search_reddit_topic(
    query: str,
    max_results: int = 20,
    api_key: Optional[str] = None,
    entity_id: Optional[str] = None,
) -> list:
    """
    Search Reddit for a topic.

    Args:
        query: Search query
        max_results: Maximum results
        api_key: Composio API key (uses env if not provided)
        entity_id: Composio Entity/User ID (uses env if not provided)

    Returns:
        List of parsed Reddit posts with metrics
    """
    if not api_key:
        api_key = get_composio_api_key()
    if not entity_id:
        entity_id = get_entity_id()

    response = search_reddit(
        api_key=api_key,
        entity_id=entity_id,
        query=query,
        max_results=max_results,
    )

    posts = parse_reddit_response(response)
    posts = enrich_with_metrics(posts)

    return posts


if __name__ == "__main__":
    import sys

    api_key = get_composio_api_key()
    entity_id = get_entity_id()

    query = sys.argv[1] if len(sys.argv) > 1 else "AI"
    results = search_reddit_topic(query, api_key=api_key, entity_id=entity_id)

    print(f"Found {len(results)} posts:")
    for post in results[:5]:
        print(f"  - {post['title'][:80]}... ({post.get('engagement', 0)} engagement)")

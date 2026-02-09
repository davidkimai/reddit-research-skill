#!/usr/bin/env python3
"""
Twitter/X search via Composio.

Uses Composio's Twitter toolkit to search X without direct API keys.
Composio v3 uses entityId instead of userId or connectionId.
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


def get_entity_id() -> str:
    """Get Composio Entity/User ID from environment."""
    return os.environ.get("COMPOSIO_USER_ID", "pg-test-YOUR-USER-ID")


def search_twitter(
    api_key: str,
    entity_id: str,
    query: str,
    max_results: int = 10,
) -> dict:
    """
    Search Twitter via Composio.

    Composio v3 uses entityId instead of userId or connectionId.
    No connected account needed - Composio manages authenticated sessions.

    Args:
        api_key: Composio API key
        entity_id: Composio Entity/User ID
        query: Search query
        max_results: Maximum number of results (minimum 10 for Composio)

    Returns:
        Composio API response
    """
    import httpx

    base_url = "https://backend.composio.dev/api"

    body = {
        "appName": "TWITTER",
        "entityId": entity_id,
        "input": {
            "query": query,
            "max_results": max_results,
        },
    }

    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json",
    }

    with httpx.Client(timeout=60.0) as client:
        response = client.post(
            f"{base_url}/v2/actions/TWITTER_RECENT_SEARCH/execute",
            headers=headers,
            json=body,
        )

        # Composio returns JSON directly
        result = response.json()

        if not result.get("success") and result.get("error"):
            raise Exception(f"Composio error: {result.get('error')}")

        return result.get("data", {})


def parse_twitter_response(response: dict) -> list:
    """
    Parse Composio Twitter response into standardized format.

    Args:
        response: Composio API response

    Returns:
        List of parsed tweets
    """
    tweets = []

    data = response.get("data", response)
    items = data if isinstance(data, list) else data.get("data", [])

    for item in items:
        tweets.append({
            "id": item.get("id", ""),
            "text": item.get("text", ""),
            "author_id": item.get("author_id", ""),
            "username": "",  # Will be filled from includes
            "name": "",
            "created_at": item.get("created_at", ""),
            "metrics": {
                "likes": item.get("public_metrics", {}).get("like_count", 0),
                "retweets": item.get("public_metrics", {}).get("retweet_count", 0),
                "replies": item.get("public_metrics", {}).get("reply_count", 0),
                "impressions": item.get("public_metrics", {}).get("impression_count", 0),
            },
            "urls": [],
            "mentions": [],
            "hashtags": [],
            "tweet_url": "",
        })

    # Fill in user info from includes
    users = response.get("includes", {}).get("users", [])
    user_map = {u.get("id"): u for u in users}

    for tweet in tweets:
        user = user_map.get(tweet.get("author_id"), {})
        tweet["username"] = user.get("username", "")
        tweet["name"] = user.get("name", "")

        # Build tweet URL
        username = user.get("username", "unknown")
        tweet["tweet_url"] = f"https://x.com/{username}/status/{tweet['id']}"

    return tweets


def enrich_tweets(tweets: list) -> list:
    """Add engagement metrics to tweets."""
    enriched = []
    for tweet in tweets:
        m = tweet.get("metrics", {})
        engagement = m.get("likes", 0) + m.get("retweets", 0) * 2 + m.get("replies", 0)
        tweet["engagement"] = engagement
        enriched.append(tweet)
    return enriched


def search_twitter_topic(
    query: str,
    max_results: int = 20,
    api_key: Optional[str] = None,
    entity_id: Optional[str] = None,
) -> list:
    """
    Search Twitter for a topic.

    Args:
        query: Search query
        max_results: Maximum results (minimum 10 for Composio)
        api_key: Composio API key (uses env if not provided)
        entity_id: Composio Entity/User ID (uses env if not provided)

    Returns:
        List of parsed tweets with metrics
    """
    if not api_key:
        api_key = get_composio_api_key()
    if not entity_id:
        entity_id = get_entity_id()

    # Composio requires minimum 10 results
    max_results = max(max_results, 10)

    response = search_twitter(
        api_key=api_key,
        entity_id=entity_id,
        query=query,
        max_results=max_results,
    )

    tweets = parse_twitter_response(response)
    tweets = enrich_tweets(tweets)

    return tweets


if __name__ == "__main__":
    import sys

    api_key = get_composio_api_key()
    entity_id = get_entity_id()

    query = sys.argv[1] if len(sys.argv) > 1 else "AI"
    results = search_twitter_topic(query, api_key=api_key, entity_id=entity_id)

    print(f"Found {len(results)} tweets:")
    for tweet in results[:5]:
        print(f"  @{tweet['username']}: {tweet['text'][:80]}... ({tweet.get('engagement', 0)} engagement)")

"""
Instagram Graph API client.
Fetches account info, media list, and per-reel insights.

All calls require a valid User Access Token from the creator's
connected Instagram Business/Creator account.
"""
import httpx
from typing import Optional

GRAPH_BASE = "https://graph.instagram.com"
GRAPH_V = "v21.0"


class InstagramClient:

    def __init__(self, access_token: str):
        self.token = access_token
        self._client = httpx.Client(timeout=15)

    # ── Account ─────────────────────────────────────────────────────────────

    def get_me(self) -> dict:
        """Return basic account info to verify the token is valid."""
        r = self._client.get(
            f"https://graph.instagram.com/me",
            params={
                "fields": "id,name,username,profile_picture_url,followers_count,media_count,account_type",
                "access_token": self.token,
            },
        )
        r.raise_for_status()
        return r.json()

    # ── Media list ───────────────────────────────────────────────────────────

    def get_reels(self, ig_user_id: str, limit: int = 25) -> list[dict]:
        """Fetch recent media, return only REELS with basic metrics."""
        r = self._client.get(
            f"https://graph.instagram.com/{ig_user_id}/media",
            params={
                "fields": (
                    "id,caption,media_type,timestamp,permalink,"
                    "thumbnail_url,media_url,"
                    "like_count,comments_count"
                ),
                "limit": limit,
                "access_token": self.token,
            },
        )
        r.raise_for_status()
        data = r.json().get("data", [])
        return [m for m in data if m.get("media_type") == "REELS"]

    # ── Reel insights ────────────────────────────────────────────────────────

    def get_reel_insights(self, media_id: str) -> dict:
        """
        Fetch reach, plays, avg watch time for a single reel.
        Requires the account to be Business/Creator.
        """
        metrics = [
            "reach", "plays", "saved",
            "ig_reels_avg_watch_time",
            "ig_reels_video_view_total_time",
            "total_interactions",
        ]
        try:
            r = self._client.get(
                f"https://graph.instagram.com/{media_id}/insights",
                params={
                    "metric": ",".join(metrics),
                    "access_token": self.token,
                },
            )
            r.raise_for_status()
            raw = r.json().get("data", [])
            return {item["name"]: item["values"][0]["value"] if item.get("values") else item.get("value", 0) for item in raw}
        except Exception:
            # Insights may not always be available (e.g. personal accounts)
            return {}

    def close(self):
        self._client.close()

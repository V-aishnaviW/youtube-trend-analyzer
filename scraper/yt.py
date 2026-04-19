# src/yt.py
from googleapiclient.discovery import build
import re
from isodate import parse_duration
from datetime import datetime

API_KEY = "AIzaSyAh0W2Iy2fo2XdbKqKNjwRrd5P5BYHclsM"
youtube = build("youtube", "v3", developerKey=API_KEY)


def extract_hashtags(title, description):
    """Extract unique hashtags from title + description"""
    text = f"{title} {description}"
    hashtags = re.findall(r"#(\w+)", text)
    hashtags = [tag.lower() for tag in hashtags]
    return list(set(hashtags))


def fetch_videos(query="shorts", max_results=50, shorts_only=True):
    """
    Fetch general videos or Shorts by search query.
    If shorts_only=True, filters videos <= 60s
    """
    videos_data = []

    # 1️⃣ Search API
    search_request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=max_results,
        order="date"
    )
    search_response = search_request.execute()

    video_ids = [item["id"]["videoId"] for item in search_response["items"]]

    if not video_ids:
        return []

    # 2️⃣ Videos API for stats + contentDetails
    videos_request = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=",".join(video_ids)
    )
    videos_response = videos_request.execute()

    for item in videos_response["items"]:
        snippet = item["snippet"]
        stats = item.get("statistics", {})
        content = item.get("contentDetails", {})

        # Duration in seconds
        duration_iso = content.get("duration", "PT0S")
        duration_sec = parse_duration(duration_iso).total_seconds()

        # Filter Shorts if requested
        if shorts_only and duration_sec > 60:
            continue

        video_id = item["id"]
        title = snippet["title"]
        description = snippet.get("description", "")
        channel_id = snippet["channelId"]
        channel_name = snippet["channelTitle"]
        published_at = snippet["publishedAt"]
        category_id = snippet.get("categoryId")

        views = int(stats.get("viewCount", 0))
        likes = int(stats.get("likeCount", 0))
        comments = int(stats.get("commentCount", 0))

        hashtags = extract_hashtags(title, description)

        video = {
            "video_id": video_id,
            "title": title,
            "channel_id": channel_id,
            "channel_name": channel_name,
            "published_at": published_at,
            "views": views,
            "likes": likes,
            "comments": comments,
            "duration": duration_sec,
            "category_id": category_id,
            "hashtags": hashtags
        }
        videos_data.append(video)

    return videos_data


if __name__ == "__main__":
    videos = fetch_videos(query="shorts", max_results=50, shorts_only=True)
    for v in videos[:5]:
        print(f"{v['title']} | {v['duration']}s | Views: {v['views']} | Hashtags: {v['hashtags']}")
    print(f"Total videos fetched: {len(videos)}")
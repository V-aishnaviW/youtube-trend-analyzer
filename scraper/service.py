# src/service.py
from scraper.repository import (
    insert_channel, insert_video, insert_category, insert_video_category,
    insert_hashtags_batch, insert_video_hashtags_batch, insert_video_snapshot
)
from datetime import datetime

def save_videos(videos_list):
    """
    Save full video data (channels, videos, categories, hashtags, snapshots)
    """
    for video in videos_list:
        # 1️⃣ Channel
        insert_channel(video["channel_id"], video["channel_name"])

        # 2️⃣ Video
        insert_video(video)

        # 3️⃣ Categories
        if video.get("category_id") and video.get("category_name"):
            insert_category(video["category_id"], video["category_name"])
            insert_video_category(video["video_id"], video["category_id"])

        # 4️⃣ Hashtags
        hashtags = video.get("hashtags", [])
        mapping = insert_hashtags_batch(hashtags)
        hashtag_ids = [mapping[tag] for tag in hashtags]
        insert_video_hashtags_batch(video["video_id"], hashtag_ids)

        # 5️⃣ Snapshot
        insert_video_snapshot(
            video_id=video["video_id"],
            views=video["views"],
            likes=video["likes"],
            comments=video["comments"],
            scraped_at=datetime.now()
        )
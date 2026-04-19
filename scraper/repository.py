# src/repository.py
from scraper.db import get_connection
#from repository import get_existing_video_ids

# --- Channels ---
def insert_channel(channel_id, channel_name):
    with get_connection() as conn:
        conn.execute("""
            INSERT OR IGNORE INTO channels (channel_id, channel_name)
            VALUES (?, ?)
        """, (channel_id, channel_name))

# --- Videos ---
def insert_video(video):
    with get_connection() as conn:
        conn.execute("""
            INSERT OR IGNORE INTO videos
            (video_id, title, published_at, duration, channel_id)
            VALUES (?, ?, ?, ?, ?)
        """, (
            video["video_id"],
            video["title"],
            video["published_at"],
            video["duration"],
            video["channel_id"]
        ))

# --- Categories ---
def insert_category(category_id, category_name):
    with get_connection() as conn:
        conn.execute("""
            INSERT OR IGNORE INTO categories (category_id, category_name)
            VALUES (?, ?)
        """, (category_id, category_name))

def insert_video_category(video_id, category_id):
    with get_connection() as conn:
        conn.execute("""
            INSERT OR IGNORE INTO video_categories (video_id, category_id)
            VALUES (?, ?)
        """, (video_id, category_id))

# --- Hashtags ---
def insert_hashtags_batch(hashtags):
    """
    Insert hashtags and return dict {hashtag_name: hashtag_id}
    """
    mapping = {}
    with get_connection() as conn:
        for tag in hashtags:
            conn.execute("""
                INSERT OR IGNORE INTO hashtags (hashtag_name)
                VALUES (?)
            """, (tag,))
            cursor = conn.execute("SELECT hashtag_id FROM hashtags WHERE hashtag_name = ?", (tag,))
            mapping[tag] = cursor.fetchone()["hashtag_id"]
    return mapping

def insert_video_hashtags_batch(video_id, hashtag_ids):
    with get_connection() as conn:
        conn.executemany("""
            INSERT OR IGNORE INTO video_hashtags (video_id, hashtag_id)
            VALUES (?, ?)
        """, [(video_id, hid) for hid in hashtag_ids])

# --- Video Snapshots ---
def insert_video_snapshot(video_id, views, likes, comments, scraped_at):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO video_snapshots
            (video_id, views, likes, comments, scraped_at)
            VALUES (?, ?, ?, ?, ?)
        """, (video_id, views, likes, comments, scraped_at))
# run_daily.py
from scraper.db import init_db
from scraper.yt import fetch_videos
from scraper.service import save_videos

# 1️⃣ Initialize DB with WAL mode
init_db()

# 2️⃣ Keywords and regions to scrape
KEYWORDS = ["shorts", "funny", "music", "ai"]
REGIONS = ["IN", "US", "GB"]  # add more as needed

# 3️⃣ Category mapping
CATEGORY_MAP = {
    "28": "Science & Technology",
    "24": "Entertainment",
    "10": "Music",
    "22": "People & Blogs",
    "26": "Howto & Style",
    "23": "Comedy",
    "17": "Sports",
    "27": "Education"
}

all_videos = []

# 4️⃣ Fetch videos for each keyword + region
for region in REGIONS:
    for keyword in KEYWORDS:
        print(f"Fetching '{keyword}' videos from region {region}...")
        videos = fetch_videos(query=keyword, max_results=50, shorts_only=True)
        for v in videos:
            v["category_name"] = CATEGORY_MAP.get(v["category_id"], "Other")
        all_videos.extend(videos)

# 5️⃣ Save all fetched videos to DB
save_videos(all_videos)

print(f"Completed! Total unique videos fetched: {len(all_videos)}")
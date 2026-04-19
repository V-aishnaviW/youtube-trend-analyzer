-- channels table
CREATE TABLE IF NOT EXISTS channels (
    channel_id TEXT PRIMARY KEY,
    channel_name TEXT
);

-- videos table (static data)
CREATE TABLE IF NOT EXISTS videos (
    video_id TEXT PRIMARY KEY,
    title TEXT,
    published_at TIMESTAMP,
    duration INTEGER,
    channel_id TEXT,
    FOREIGN KEY (channel_id) REFERENCES channels(channel_id)
);

-- categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT UNIQUE
);

-- hashtags table
CREATE TABLE IF NOT EXISTS hashtags (
    hashtag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hashtag_name TEXT UNIQUE
);

-- video_categories junction table
CREATE TABLE IF NOT EXISTS video_categories (
    video_id TEXT,
    category_id INTEGER,
    PRIMARY KEY (video_id, category_id),
    FOREIGN KEY (video_id) REFERENCES videos(video_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- video_hashtags junction table
CREATE TABLE IF NOT EXISTS video_hashtags (
    video_id TEXT,
    hashtag_id INTEGER,
    PRIMARY KEY (video_id, hashtag_id),
    FOREIGN KEY (video_id) REFERENCES videos(video_id),
    FOREIGN KEY (hashtag_id) REFERENCES hashtags(hashtag_id)
);

-- snapshot table (daily metrics)
CREATE TABLE IF NOT EXISTS video_snapshots (
    snapshot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id TEXT,
    views INTEGER,
    likes INTEGER,
    comments INTEGER,
    scraped_at TIMESTAMP,
    FOREIGN KEY (video_id) REFERENCES videos(video_id)
);
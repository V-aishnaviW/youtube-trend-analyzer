import sqlite3

conn = sqlite3.connect("youtube_trends.db")
cursor = conn.cursor()

with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

conn.commit()
conn.close()

print("Database schema created successfully!")
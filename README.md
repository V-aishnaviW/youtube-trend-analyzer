# 📱 YouTube Shorts Trend Analyzer

## 🚀 Overview
This project collects YouTube Shorts data using the YouTube Data API, stores it in a normalized SQLite database, and analyzes trends such as viral topics, posting time, and engagement.

---

## 🎯 Project Goal
To build a data pipeline that:
- Collects YouTube Shorts data daily
- Stores structured data using a normalized schema
- Enables trend analysis using SQL

---

## ⚙️ Features
- 📥 Automated data collection (manual trigger)
- 🧠 Normalized database design (3NF)
- ⏱ Time-series tracking using snapshots
- 🔍 Hashtag extraction and analysis
- 📊 SQL-based trend analysis (in progress)

---

## 🏗️ Architecture

Scraper (yt.py)
↓
Service Layer (service.py)
↓
Repository Layer (repository.py)
↓
SQLite Database


---

## 🛠 Tech Stack
- Python
- SQLite
- YouTube Data API
- SQL

---

## 📂 Project Structure

trend-analyzer/
│
├── src/
│ ├── yt.py
│ ├── db.py
│ ├── repository.py
│ └── service.py
│
├── schema.sql
├── run_daily.py
├── Create_db.py
└── .gitignore

---

## 📊 Current Status
- ✅ Data Collection & Storage Completed
- 🚧 Data Analysis in Progress
- ⏳ Dashboard & Insights Planned

---

## ▶️ How to Run

1. Install dependencies:pip install -r requirements.txt

2. Set your API key:export YOUTUBE_API_KEY= "my_yt_key"

3. Run scraper:python run_daily.py


---

## 📈 Sample Queries

```sql
-- Total videos collected
SELECT COUNT(*) FROM videos;

-- Total snapshots collected
SELECT COUNT(*) FROM video_snapshots;


🔮 Future Improvements
Interactive dashboard (Streamlit / Power BI)
Machine learning for trend prediction

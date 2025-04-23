import os
from dotenv import load_dotenv

# Load .env file if available
load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
TARGET_SUBREDDIT = os.getenv("TARGET_SUBREDDIT")
DAYS_LOOKBACK = int(os.getenv("DAYS_LOOKBACK", "1"))

RSS_FEEDS = [
    "https://www.indiatoday.in/rss/1206814",
    "https://timesofindia.indiatimes.com/rssfeeds/-2128672765.cms",
    "https://www.thehindu.com/sci-tech/science/feeder/default.rss"
]

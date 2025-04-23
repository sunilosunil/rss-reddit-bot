import feedparser
from datetime import datetime, timedelta
from dateutil import parser as date_parser
import praw
import config

def fetch_recent_articles(rss_urls, days=1):
    recent_articles = []
    now = datetime.utcnow()
    time_threshold = now - timedelta(days=days)

    for url in rss_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            published = None
            if 'published' in entry:
                published = date_parser.parse(entry.published)
            elif 'updated' in entry:
                published = date_parser.parse(entry.updated)
            else:
                continue

            if published > time_threshold:
                title = entry.get('title', 'No Title')
                link = entry.get('link', 'No Link')
                recent_articles.append((title, link))
    return recent_articles

def post_to_subreddit(articles, subreddit_name):
    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        username=config.REDDIT_USERNAME,
        password=config.REDDIT_PASSWORD,
        user_agent=config.REDDIT_USER_AGENT
    )

    for title, link in articles:
        try:
            print(f"Posting: {title}")
            reddit.subreddit(subreddit_name).submit(title=title, url=link)
        except Exception as e:
            print(f"Error posting '{title}': {e}")

def main():
    articles = fetch_recent_articles(config.RSS_FEEDS, config.DAYS_LOOKBACK)
    post_to_subreddit(articles, config.TARGET_SUBREDDIT)

if __name__ == "__main__":
    main()

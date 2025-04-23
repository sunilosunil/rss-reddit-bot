# 🤖 RSS to Reddit Bot

This bot fetches the latest science articles from popular RSS feeds and posts them to a subreddit using [PRAW](https://praw.readthedocs.io/en/latest/). It supports local development with a `.env` file and automated daily posting via GitHub Actions.

---

## 🚀 Features

- Fetches articles from:
  - India Today Science
  - Times of India Science
  - The Hindu Science
- Filters posts from the last `X` days
- Posts to Reddit via PRAW
- Scheduled daily using GitHub Actions
- Secrets managed via `.env` (local) and GitHub Secrets (CI/CD)

---

## 🧰 Requirements

- Python 3.7+
- Reddit account
- Subreddit where you have permission to post

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/rss_to_reddit_bot.git
cd rss_to_reddit_bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Getting Reddit API Credentials

1. Visit: [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Scroll to the bottom and click **“create another app...”**
3. Fill out:
   - **name**: RSS Reddit Bot
   - **type**: `script`
   - **redirect uri**: `http://localhost`
4. Save and note:
   - `client_id`: the string below the app name
   - `client_secret`: the generated secret

---

## ✍️ Create `.env` File (for Local Testing)

Create a file named `.env` in the root folder:

```env
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
REDDIT_USER_AGENT=script:science_rss_bot:v1.0 (by u/your_reddit_username)
TARGET_SUBREDDIT=your_target_subreddit
DAYS_LOOKBACK=1
```

Then run the bot locally:

```bash
python science_rss_bot.py
```

---

## 🔄 Set Up GitHub Secrets for Automation

In your GitHub repository:

1. Go to **Settings > Secrets > Actions**
2. Click **New repository secret** and add:

| Secret Name              | Value from your `.env` file               |
|--------------------------|-------------------------------------------|
| `REDDIT_CLIENT_ID`       | `your_client_id`                         |
| `REDDIT_CLIENT_SECRET`   | `your_client_secret`                     |
| `REDDIT_USERNAME`        | `your_reddit_username`                   |
| `REDDIT_PASSWORD`        | `your_reddit_password`                   |
| `REDDIT_USER_AGENT`      | `script:science_rss_bot:v1.0 ...`        |
| `TARGET_SUBREDDIT`       | `your_target_subreddit`                  |
| `DAYS_LOOKBACK`          | `1` (or any number of days to look back) |

---

## 🕒 Scheduled Automation (GitHub Actions)

The included GitHub Action `.github/workflows/daily.yml` runs the bot daily at 14:00 UTC.

You can trigger it manually from the Actions tab as well.

---

## 🧪 To Test Locally

```bash
python science_rss_bot.py
```

Make sure `.env` is correctly set.

---

## ✅ TODO / Improvements

- Avoid posting duplicate articles
- Add support for different categories or feeds
- Add logging and error tracking

---

## 📄 License

MIT License

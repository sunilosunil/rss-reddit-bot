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

## 🛠️ Local Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/rss_to_reddit_bot.git
cd rss_to_reddit_bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` File (for Local Testing)

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
python rss_bot.py
```

---

## 🔐 How to Get Reddit API Credentials

1. Log in to your Reddit account.
2. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
3. Scroll to the bottom and click **“create another app...”**
4. Fill out the form:
   - **name**: RSS Reddit Bot
   - **type**: `script`
   - **description**: (optional)
   - **redirect uri**: `http://localhost`
5. Click **Create app**
6. Save the following values:
   - `client_id`: shown just under the app name
   - `client_secret`: shown after clicking “edit”
   - Your Reddit **username** and **password** will be used for script authentication
   - Use a meaningful `user_agent` (e.g. `script:science_rss_bot:v1.0 (by u/yourname)`)

---

## 🔄 How It Runs with GitHub Actions

This project includes a GitHub Actions workflow file located at:

```
.github/workflows/daily.yml
```

### What it does:
- Checks out your code daily at 14:00 UTC
- Installs dependencies from `requirements.txt`
- Runs `rss_bot.py` with credentials loaded from GitHub Secrets

### Running Automatically:
1. Push this repository to GitHub.
2. Go to your repo → **Settings → Secrets → Actions**
3. Add these secrets (copy values from your `.env`):

| Secret Name              | Value                              |
|--------------------------|------------------------------------|
| `REDDIT_CLIENT_ID`       | your Reddit app client_id          |
| `REDDIT_CLIENT_SECRET`   | your Reddit app client_secret      |
| `REDDIT_USERNAME`        | your Reddit username               |
| `REDDIT_PASSWORD`        | your Reddit password               |
| `REDDIT_USER_AGENT`      | e.g. script:science_rss_bot:v1.0   |
| `TARGET_SUBREDDIT`       | e.g. mysciencefeed                 |
| `DAYS_LOOKBACK`          | 1 (or number of days to look back) |

### Manual Trigger
You can also trigger the workflow manually from the **Actions** tab in GitHub.

---

## ✅ TODO / Improvements
- Add logging or daily summary
- Support for more feeds or subreddit rules

---

## 📄 License

MIT License

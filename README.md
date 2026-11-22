# 100 Days of Python Tracker

A digital version of the 100 Days of Python check-off poster. It also tracks
the real time each course day took, because one "day" of the course can take
a week of 20-minute sessions.

- **Tap a day** to see which dates you worked on it and the minutes logged for each
- **Right-click a day** to mark it complete

Built from scratch as part of my WGU Python coursework.

**Stack:** Python (FastAPI) on Cloudflare Workers, a D1 (SQLite) database, and HTML/CSS/JS.

See [LEARNING_PLAN.md](LEARNING_PLAN.md) for the build roadmap.

## Run locally

```powershell
uv run pywrangler dev
```

## Deploy

```powershell
uv run pywrangler deploy
```

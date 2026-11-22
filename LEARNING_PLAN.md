# Learning plan

You write the code. This file is the map. Each milestone has a goal, the
`TODO` labels it unlocks in the code, questions to answer **before** typing,
and hints folded away. Open a hint only after you've been stuck for 10 minutes.

## The stack, and why

```
 phone browser ──► https://100days.shawtechlab.com
                         │
                  Cloudflare Worker
                  ├── public/      HTML + CSS + a little JS   (what you see)
                  ├── src/main.py  FastAPI, plain functions    (the rules)
                  └── D1           SQLite database            (the memory)
```

| Piece | What it is | Why this one |
|---|---|---|
| **Python + FastAPI** | Your web API. Each URL is a function with a decorator. | It's the course language, and you need no classes. Cloudflare runs it natively. |
| **D1** | SQLite hosted by Cloudflare. | It's real SQL, which you'll meet in the course anyway. Your data lives in one place, so your phone and PC see the same thing. |
| **HTML/CSS/JS** | The poster you tap. | A browser only speaks these. Keep the JS thin and put the logic in Python. |
| **Workers + custom domain** | The hosting. | You already pay for it, it never sleeps, and wrangler creates the DNS record for you. |

**Python Workers quirk to know:** your Python runs inside the browser-style
engine (Pyodide), not on a normal server. Talking to D1 means `await`-ing
calls, and results sometimes come back as JavaScript objects you convert with
`.to_py()`. That's the one unusual thing about this stack. Everything else is
normal Python.

## How to run it

```powershell
uv run pywrangler dev          # local server at http://localhost:8787
uv run pywrangler deploy       # push live to 100days.shawtechlab.com
```

## Your 20-minute session ritual

1. Open this file and find the first unchecked box.
2. Work on only that box. If 20 minutes runs out mid-box, write one line in
   `NOTES.md` saying where you stopped and what you were about to try.
3. `git add -A` then `git commit -m "..."`. A small commit every session is the habit.

Once Milestone 3 is done, log those 20 minutes in the app itself.

---

## Milestone 0: hello, phone
- [ ] Run `uv run pywrangler dev` and open http://localhost:8787/api/health
- [ ] Open https://100days.shawtechlab.com/api/health **on your phone**
- [ ] Change the health message, deploy, and see it change on your phone

**Think:** `/api/health` ran Python, but `/` showed `index.html` without
running any Python. Find the line in `wrangler.jsonc` that decides which goes where.

## Milestone 1: design the data (`schema.sql`, TODO 1.x)
- [ ] Answer the 5 questions at the top of `schema.sql` on paper
- [ ] Write the `CREATE TABLE` statements
- [ ] Run them locally, then query: `npx wrangler d1 execute 100-days-tracker --local --command "SELECT * FROM ..."`
- [ ] Insert your real history (days 1-9)

<details><summary>Hint: how many tables?</summary>

Two. One row per **course day** (100 rows, with completed or not, and when).
One row per **coding session** (date, minutes, and which course day it was for).
Day 9 has many sessions; each session has one day. That's a *one-to-many*
relationship, and the "which day" column goes on the *many* side.
</details>

<details><summary>Hint: dates in SQLite</summary>

SQLite has no date type. Store dates as text in `YYYY-MM-DD` form. That format
sorts correctly as plain text. Why would `11/22/2026` not sort correctly?
</details>

## Milestone 2: read data (`src/main.py`, TODO 2.x)
- [ ] `GET /api/days`, returning 100 items with totals
- [ ] `GET /api/days/{day_number}`, returning one day's sessions
- [ ] Bad day numbers return a 404, not a crash

<details><summary>Hint: querying D1 from Python</summary>

```python
db = request.scope["env"].DB
result = await db.prepare("SELECT ... WHERE x = ?").bind(some_value).all()
rows = result.results.to_py()   # now a normal Python list of dicts
```
Always use `?` with `.bind()` and never paste values into the SQL with
f-strings. Look up "SQL injection" to see why.
</details>

<details><summary>Hint: totals for every day in one query</summary>

Look up `LEFT JOIN`, `GROUP BY`, `SUM()`, and `COALESCE()`. Why LEFT and not plain JOIN?
(Think about days you haven't started.)
</details>

**Write a helper function** like `fetch_all(db, sql, *params)` once you notice
you're repeating the same three lines. That's the point of functions.

## Milestone 3: write data (TODO 3.x)
- [ ] `POST /api/sessions`, with validation that rejects garbage input
- [ ] `POST /api/days/{n}/toggle-complete`
- [ ] Test both with `curl` or FastAPI's built-in `/docs` page before any UI exists

## Milestone 4: the poster (`public/`, TODO 4.x)
- [ ] JS builds the 100 squares from `/api/days`
- [ ] CSS lays them out like the poster (7 columns, numbers flow down)
- [ ] Complete days are green with ✓; in-progress days get a color you choose

## Milestone 5: interaction (TODO 5.x)
- [ ] Tap a day to open details (dates, minutes per session, totals)
- [ ] Right-click a day to toggle complete
- [ ] **Test on your actual phone.** Solve the "phones have no right-click" problem.
- [ ] Log-a-session form inside the details panel

## Milestone 6: stats and summary (TODO 6.x)
One `GET /api/stats` route, built out of many small functions, one per number.
That's the best function practice in the whole project.

- [ ] Start date (first session ever) and days elapsed since then
- [ ] Course days complete, as a count and a %
- [ ] Total hours logged, and average minutes per completed course day
- [ ] **Average real calendar days per course day** (day 9 took ~30)
- [ ] **Projected finish date** = today + (days remaining × that average)
- [ ] Current streak and longest streak of ≥ 20-minute calendar days (TODO 6.1)
- [ ] Hardest day so far (most minutes)

**Think:** you finished days 1-8 fast and day 9 slow. Should the projection use
your all-time average or only your last 5 completed days? Try both and see
which number you believe. Later course days are longer projects, so an honest
projection probably gets *later* over time. That's fine: it's data, not a judgment.

**Think:** "real days to complete day 9": count from when day 8 was completed?
Or from day 9's first session? These give different answers. Pick one and
write down why.

## Milestone 7: stretch goals
- [ ] Habit heatmap: a small calendar grid (like GitHub's contribution graph)
      where each square is a real calendar date, colored by minutes logged.
      Green for ≥ 20. This shows your *habit*, while the poster shows *progress*.
- [ ] Quick-log button on the home screen: "+20 min on my current day" in one tap
- [ ] Notes field per session ("finally got the recursion to click")
- [ ] Export everything to CSV (practice for the WGU data-handling units)
- [ ] Lock it down so only you can edit (ask me about Cloudflare Access when you get here)
- [ ] Add to home screen on your phone so it opens like an app
- [ ] A notes field per session ("finally got the recursion to click")

"""
100 Days of Code tracker: the Python side (the API).

The browser never touches the database directly. It asks THIS file for data
by calling URLs like /api/days. Each URL is one function you write below.

Rules for this project: functions only, no classes.

Platform note (not something to figure out yourself): inside any route,
your database is available as:

    db = request.scope["env"].DB

You'll learn how to query it in LEARNING_PLAN.md, Milestone 2.
"""

from fastapi import FastAPI, Request
from workers import asgi

app = FastAPI()


# This one works already, so you can prove the deploy pipeline before writing
# any real code. Visit https://100days.shawtechlab.com/api/health
@app.get("/api/health")
async def health():
    return {"ok": True}


# ---------------------------------------------------------------------------
# MILESTONE 2: read data
# ---------------------------------------------------------------------------

# TODO 2.1: GET /api/days
#   Return all 100 days. For each one the poster needs to know:
#   the day number, whether it's complete, and the total minutes logged.
#   Think: if you've never logged time on day 57, does day 57 still show up?
#   (It has to. The poster has 100 squares no matter what.)

# TODO 2.2: GET /api/days/{day_number}
#   Return the details for ONE day: every session you logged against it
#   (date and minutes), plus totals: number of sessions and total minutes.
#   Think: what should happen if someone asks for day 0 or day 250?


# ---------------------------------------------------------------------------
# MILESTONE 3: write data
# ---------------------------------------------------------------------------

# TODO 3.1: POST /api/sessions
#   Log a coding session: which day it counts toward, the date, and the minutes.
#   Think: what input should you REJECT? (negative minutes? 900 minutes?
#   a day that's already marked complete?)

# TODO 3.2: POST /api/days/{day_number}/toggle-complete
#   Flip a day between complete and not complete. Record WHEN it was completed.
#   Think: why "toggle" instead of only "complete"? (What if you misclick?)


# ---------------------------------------------------------------------------
# MILESTONE 6: stats and summary
# ---------------------------------------------------------------------------

# TODO 6.0: GET /api/stats
#   Return one dict of summary numbers (see LEARNING_PLAN.md for the list).
#   Don't write one giant function. Write one small function per stat,
#   e.g. average_real_days_per_course_day(...), projected_finish_date(...),
#   and have this route just call them and collect the results.
#   Bonus: most of those small functions don't need the database at all if
#   you pass them a list of rows. That makes them easy to test with plain Python.

# TODO 6.1: current_streak(...) and longest_streak(...)
#   How many calendar days in a row (ending today) did you log >= 20 minutes?
#   Note this is a DIFFERENT question than "which course day are you on".
#   This one is the heart of why you're building this app.


# Hands your FastAPI app to Cloudflare. Leave this as the last line.
Default = asgi.entrypoint(app)

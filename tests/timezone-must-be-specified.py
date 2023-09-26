from datetime import datetime, timedelta, timezone

# ruleid: timezone-must-be-specified
bad = datetime.now()

the_best = datetime.now(timezone.utc)
okay_but_format_sucks = datetime.now(tz=timezone.utc)

# Works fine too
moscow = timezone(timedelta(hours=3), "moscow")
nice = datetime.now(moscow)

# This is the intended way if you want a local naive datetime.
naive_local = datetime.now(moscow).replace(tzinfo=None)

from datetime import datetime, timedelta, timezone

# ruleid: timezone-must-be-specified
bad = datetime.now()

# ok: timezone-must-be-specified
the_best = datetime.now(timezone.utc)

# ok: timezone-must-be-specified
okay_but_format_sucks = datetime.now(tz=timezone.utc)

moscow = timezone(timedelta(hours=3), "moscow")
# ok: timezone-must-be-specified
nice = datetime.now(moscow)

# This is the intended way if you want a local naive datetime.
# ok: timezone-must-be-specified
naive_local = datetime.now(moscow).replace(tzinfo=None)

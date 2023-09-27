from typing import Any, Dict, List

# ruleid: empty-collection-type-hint
bad = []

# ruleid: empty-collection-type-hint
another_bad = {}


# Another rule should catch non-parametrized type hint
# ok: empty-collection-type-hint
okayish: list = []

# ok: empty-collection-type-hint
good = [1, 2, 3]

# ok: empty-collection-type-hint
very_good: List[List[List[int]]] = [[[1]]]

# Same as with list.
# ok: empty-collection-type-hint
weird_but_ok: dict = {}

# ok: empty-collection-type-hint
nice_bot_avoid_any_please: Dict[str, Any] = {"5": 3}

# ok: empty-collection-type-hint
acceptable = {"5": 3}

from typing import Any, Dict, List

# ruleid: empty-collection-type-hint
bad = []

# ruleid: empty-collection-type-hint
another_bad = {}

okayish_and_we_hope_for_another_warning: list = []
good = [1, 2, 3]
very_good: List[List[List[int]]] = [[[1]]]

weird_but_ok: dict = {}
nice_bot_avoid_any_please: Dict[str, Any] = {"5": 3}
acceptable = {"5": 3}

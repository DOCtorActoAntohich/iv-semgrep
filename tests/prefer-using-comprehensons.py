from typing import List, Callable

# Imagine some big list that you don't want store fully in memory,
# And now you need to process its elements.
big_thing = range(1, 100000)

# If you wanted to get away with maps, then congrats, you won't.
# ruleid: prefer-using-comprehensons
bad_idea = map(lambda x: x * x, big_thing)

# Nor with filters :trol face:
# ruleid: prefer-using-comprehensons
still_bad_idea = filter(lambda x: x % 2 == 0, bad_idea)

# This is not tuple, but generator expression, which is still small.
good_idea = (x * x for x in big_thing)
still_good_idea = (x for x in good_idea if x % 2 == 0)


class Moger:
    def __init__(self, values: List[int]) -> None:
        self.values = values

    def filter(self, predicate: Callable[[int], bool]) -> "Moger":
        self.values = [value for value in self.values if predicate(value)]
        return self


weirdly_okay = Moger(list(range(10))).filter(lambda x: x % 2 == 0).values

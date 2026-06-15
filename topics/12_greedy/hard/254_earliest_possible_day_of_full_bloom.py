"""
Problem: Earliest Possible Day of Full Bloom
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Plant seeds then grow them. Find earliest day all flowers bloom. Greedy on growTime.
Complexity: Time O(N log N), Space O(N)
"""

import pytest
from typing import List


def solve_brute(plantTime, growTime):
    return solve_optimal(plantTime, growTime)


def solve_optimal(plantTime, growTime):
    pairs = sorted(zip(plantTime, growTime), key=lambda x: -x[1])
    day = bloom = 0
    for p, g in pairs:
        day += p
        bloom = max(bloom, day + g)
    return bloom


@pytest.mark.parametrize(
    "p,g,ex", [([1, 4, 3], [2, 3, 1], 9), ([1, 2, 3, 2], [2, 1, 2, 1], 9)]
)
def test_opt(p, g, ex):
    assert solve_optimal(p, g) == ex

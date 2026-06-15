"""
Problem: Find Smallest Letter Greater Than Target
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Find the smallest element in sorted char array strictly greater than target. Wraps around.
Complexity: Time O(log N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(letters, target):
    for c in letters:
        if c > target:
            return c
    return letters[0]


def solve_optimal(letters, target):
    l, r = 0, len(letters) - 1
    while l <= r:
        mid = (l + r) // 2
        if letters[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1
    return letters[l % len(letters)]


@pytest.mark.parametrize(
    "l,t,ex",
    [
        (["c", "f", "j"], "a", "c"),
        (["c", "f", "j"], "c", "f"),
        (["c", "f", "j"], "j", "c"),
    ],
)
def test_opt(l, t, ex):
    assert solve_optimal(l, t) == ex

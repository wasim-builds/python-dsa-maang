"""
Problem: Hand of Straights
Difficulty: Medium  Companies: Google,Amazon
Problem Statement: Determine if hand can be divided into groups of groupSize consecutive cards.
Complexity: Time O(N log N), Space O(N)
"""

import pytest
from typing import List
from collections import Counter


def solve_brute(hand, gs):
    return solve_optimal(hand, gs)


def solve_optimal(hand, groupSize):
    if len(hand) % groupSize:
        return False
    count = Counter(hand)
    for k in sorted(count):
        if count[k] > 0:
            times = count[k]
            for i in range(groupSize):
                if count[k + i] < times:
                    return False
                count[k + i] -= times
    return True


@pytest.mark.parametrize(
    "h,gs,ex", [([1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True), ([1, 2, 3, 4, 5], 4, False)]
)
def test_opt(h, gs, ex):
    assert solve_optimal(h, gs) == ex

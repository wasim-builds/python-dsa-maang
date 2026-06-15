"""
Problem: Last Stone Weight
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Smash two heaviest stones. Return weight of last stone or 0.
Complexity: Time O(N log N), Space O(N)
"""

import pytest, heapq
from typing import List


def solve_brute(stones):
    while len(stones) > 1:
        stones.sort()
        y, x = stones.pop(), stones.pop()
        if x != y:
            stones.append(y - x)
    return stones[0] if stones else 0


def solve_optimal(stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        y, x = -heapq.heappop(stones), -heapq.heappop(stones)
        if x != y:
            heapq.heappush(stones, -(y - x))
    return -stones[0] if stones else 0


@pytest.mark.parametrize("s,ex", [([2, 7, 4, 1, 8, 1], 1), ([1], 1)])
def test_opt(s, ex):
    assert solve_optimal(s[:]) == ex

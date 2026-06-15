"""
Problem: Last Stone Weight
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Smash two heaviest stones. Return weight of last stone or 0.
Complexity: Time O(N log N), Space O(N)
"""

import heapq
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


if __name__ == "__main__":
    test_cases = [([2, 7, 4, 1, 8, 1], 1), ([1], 1)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s, ex in test_cases:
        assert solve_optimal(s[:]) == ex
    print("All tests passed successfully!")

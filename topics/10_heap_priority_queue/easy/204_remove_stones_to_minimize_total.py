"""
Problem: Remove Stones to Minimize the Total
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Remove floor(piles[i]/2) from pile at each step, k operations. Return min total.
Complexity: Time O(k log N), Space O(N)
"""

import heapq
from typing import List


def solve_brute(piles, k):
    for _ in range(k):
        piles.sort(reverse=True)
        piles[0] -= piles[0] // 2
    return sum(piles)


def solve_optimal(piles, k):
    heap = [-p for p in piles]
    heapq.heapify(heap)
    for _ in range(k):
        p = -heapq.heappop(heap)
        heapq.heappush(heap, -(p - (p // 2)))
    return -sum(heap)


if __name__ == "__main__":
    test_cases = [([5, 4, 9], 2, 12), ([4, 3, 6, 7], 3, 12)]

    for p, k, ex in test_cases:
        assert solve_optimal(p[:], k) == ex
    print("All tests passed successfully!")

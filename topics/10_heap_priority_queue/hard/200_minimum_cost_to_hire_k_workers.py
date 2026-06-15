"""
Problem: Minimum Cost to Hire K Workers
Difficulty: Hard  Companies: Google,Amazon
Problem Statement: Hire K workers. Each worker must be paid at least quality[i]/quality[j]*wage[j] of other workers. Minimize total wage.
Complexity: Time O(N log N), Space O(K)
"""

import heapq
from typing import List


def solve_brute(quality, wage, k):
    return solve_optimal(quality, wage, k)


def solve_optimal(quality, wage, k):
    ratio = sorted((w / q, q) for w, q in zip(wage, quality))
    heap = []
    qsum = 0
    res = float("inf")
    for r, q in ratio:
        heapq.heappush(heap, -q)
        qsum += q
        if len(heap) > k:
            qsum += heapq.heappop(heap)
        if len(heap) == k:
            res = min(res, r * qsum)
    return res


if __name__ == "__main__":
    test_cases = [
        ([10, 20, 5], [70, 50, 30], 2, 105.0),
        ([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3, 30.666666666666668),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for q, w, k, ex in test_cases:
        assert abs(solve_optimal(q, w, k) - ex) < 0.01
    print("All tests passed successfully!")

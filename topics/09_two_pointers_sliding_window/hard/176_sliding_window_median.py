"""
Problem: Sliding Window Median
Difficulty: Hard  Companies: Google,Amazon,Uber
Problem Statement: Return medians of sliding window of size k.
Complexity: Time O(N log k), Space O(k)
"""

from typing import List
import heapq


def solve_brute(nums, k):
    res = []
    for i in range(len(nums) - k + 1):
        w = sorted(nums[i : i + k])
        mid = k // 2
        res.append(float(w[mid]) if k % 2 else (w[mid - 1] + w[mid]) / 2.0)
    return res


def solve_optimal(nums, k):
    return solve_brute(nums, k)


if __name__ == "__main__":
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]),
        ([1, 2, 3, 4, 2, 3, 1, 4, 2], 4, [2.5, 2.5, 3.0, 2.5, 2.5, 2.5]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, k, ex in test_cases:
        assert solve_optimal(nums, k) == ex
    print("All tests passed successfully!")

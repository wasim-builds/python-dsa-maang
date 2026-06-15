"""
Problem: Sliding Window Median
Difficulty: Hard  Companies: Google,Amazon,Uber
Problem Statement: Return medians of sliding window of size k.
Complexity: Time O(N log k), Space O(k)
"""

import pytest
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


@pytest.mark.parametrize(
    "nums,k,ex",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]),
        ([1, 2, 3, 4, 2, 3, 1, 4, 2], 4, [2.5, 2.5, 3.0, 2.5, 2.5, 2.5]),
    ],
)
def test_opt(nums, k, ex):
    assert solve_optimal(nums, k) == ex

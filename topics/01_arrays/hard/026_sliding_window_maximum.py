"""
Problem: Sliding Window Maximum
Difficulty: Hard
Topic: 01_arrays  Companies: Amazon,Google,Meta,Bloomberg
Problem Statement: Given array nums and window size k, return max of each window.
Complexity: Time O(N), Space O(k)
"""

import pytest
from typing import List
from collections import deque


def solve_brute(nums, k):
    return [max(nums[i : i + k]) for i in range(len(nums) - k + 1)]


def solve_optimal(nums, k):
    q = deque()
    res = []
    for i, n in enumerate(nums):
        while q and nums[q[-1]] <= n:
            q.pop()
        q.append(i)
        if q[0] == i - k:
            q.popleft()
        if i >= k - 1:
            res.append(nums[q[0]])
    return res


@pytest.mark.parametrize(
    "nums,k,ex", [([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]), ([1], 1, [1])]
)
def test_opt(nums, k, ex):
    assert solve_optimal(nums, k) == ex


@pytest.mark.parametrize(
    "nums,k,ex", [([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7])]
)
def test_brute(nums, k, ex):
    assert solve_brute(nums, k) == ex

"""
Problem: Jump Game VI
Difficulty: Hard  Companies: Amazon,Google,Facebook
Problem Statement: Maximize score jumping from index 0 to n-1. Can jump up to k steps.
Complexity: Time O(N), Space O(N)
"""

import pytest
from typing import List
from collections import deque


def solve_brute(nums, k):
    n = len(nums)
    dp = [float("-inf")] * n
    dp[0] = nums[0]
    for i in range(1, n):
        for j in range(max(0, i - k), i):
            dp[i] = max(dp[i], dp[j] + nums[i])
    return dp[-1]


def solve_optimal(nums, k):
    n = len(nums)
    dp = nums[:]
    q = deque([0])
    for i in range(1, n):
        while q and q[0] < i - k:
            q.popleft()
        dp[i] = dp[q[0]] + nums[i]
        while q and dp[q[-1]] <= dp[i]:
            q.pop()
        q.append(i)
    return dp[-1]


@pytest.mark.parametrize(
    "nums,k,ex", [([1, -1, -2, 4, -7, 3], 2, 7), ([10, -5, -2, 4, 0, 3], 4, 17)]
)
def test_opt(nums, k, ex):
    assert solve_optimal(nums, k) == ex


@pytest.mark.parametrize("nums,k,ex", [([1, -1, -2, 4, -7, 3], 2, 7)])
def test_brute(nums, k, ex):
    assert solve_brute(nums, k) == ex

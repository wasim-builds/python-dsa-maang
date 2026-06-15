"""
Problem: Longest Increasing Subsequence
Difficulty: Medium  Companies: Amazon,Google,Microsoft,Facebook,Bloomberg
Problem Statement: Return length of longest strictly increasing subsequence.
Complexity: Time O(N log N), Space O(N)
"""

import pytest
from typing import List
import bisect


def solve_brute(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def solve_optimal(nums):
    tails = []
    for n in nums:
        pos = bisect.bisect_left(tails, n)
        if pos == len(tails):
            tails.append(n)
        else:
            tails[pos] = n
    return len(tails)


@pytest.mark.parametrize(
    "nums,ex",
    [([10, 9, 2, 5, 3, 7, 101, 18], 4), ([0, 1, 0, 3, 2, 3], 4), ([7, 7, 7, 7, 7], 1)],
)
def test_opt(nums, ex):
    assert solve_optimal(nums) == ex

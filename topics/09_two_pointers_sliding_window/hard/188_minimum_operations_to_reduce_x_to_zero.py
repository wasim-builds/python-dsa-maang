"""
Problem: Minimum Operations to Reduce X to Zero
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Find min operations to reduce x to 0 by removing from either end.
Complexity: Time O(N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(nums, x):
    total = sum(nums)
    target = total - x
    if target < 0:
        return -1
    if target == 0:
        return len(nums)
    mp = {0: -1}
    cur = 0
    res = float("-inf")
    for i, n in enumerate(nums):
        cur += n
        if cur - target in mp:
            res = max(res, i - mp[cur - target])
        mp[cur] = i
    return len(nums) - res if res != float("-inf") else -1


def solve_optimal(nums, x):
    return solve_brute(nums, x)


@pytest.mark.parametrize(
    "nums,x,ex",
    [([1, 1, 4, 2, 3], 5, 2), ([5, 6, 7, 8, 9], 4, -1), ([3, 2, 20, 1, 1, 3], 10, 5)],
)
def test_opt(nums, x, ex):
    assert solve_optimal(nums, x) == ex

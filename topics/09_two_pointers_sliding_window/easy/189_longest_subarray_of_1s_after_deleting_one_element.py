"""
Problem: Longest Subarray of 1's After Deleting One Element
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Delete one element from binary array, return max length of subarray of 1s.
Complexity: Time O(N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(nums):
    n = len(nums)
    res = 0
    for i in range(n):
        arr = nums[:i] + nums[i + 1 :]
        cnt = cur = 0
        for x in arr:
            if x == 1:
                cur += 1
                cnt = max(cnt, cur)
            else:
                cur = 0
        res = max(res, cnt)
    return res


def solve_optimal(nums):
    l = zeros = res = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            zeros += 1
        while zeros > 1:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        res = max(res, r - l)
    return res


@pytest.mark.parametrize(
    "nums,ex", [([1, 1, 0, 1], 3), ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5), ([1, 1, 1], 2)]
)
def test_opt(nums, ex):
    assert solve_optimal(nums) == ex

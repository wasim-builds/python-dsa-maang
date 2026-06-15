"""
Problem: Squares of a Sorted Array
Difficulty: Easy  Companies: Google,Amazon,Microsoft
Problem Statement: Return sorted array of squares of sorted array.
Complexity: Time O(N), Space O(N)
"""

import pytest
from typing import List


def solve_brute(nums):
    return sorted(x * x for x in nums)


def solve_optimal(nums):
    n = len(nums)
    res = [0] * n
    l, r = 0, n - 1
    pos = n - 1
    while l <= r:
        if abs(nums[l]) >= abs(nums[r]):
            res[pos] = nums[l] * nums[l]
            l += 1
        else:
            res[pos] = nums[r] * nums[r]
            r -= 1
        pos -= 1
    return res


@pytest.mark.parametrize(
    "nums,ex",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ],
)
def test_opt(nums, ex):
    assert solve_optimal(nums) == ex

"""
Problem: Number of Subarrays with Bounded Maximum
Difficulty: Medium  Companies: Amazon,Google
Problem Statement: Return number of subarrays where max element is in range [left, right].
Complexity: Time O(N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(nums, left, right):
    cnt = 0
    for i in range(len(nums)):
        mx = 0
        for j in range(i, len(nums)):
            mx = max(mx, nums[j])
            if left <= mx <= right:
                cnt += 1
    return cnt


def solve_optimal(nums, left, right):
    def count(bound):
        res = curr = 0
        for n in nums:
            curr = curr + 1 if n <= bound else 0
            res += curr
        return res

    return count(right) - count(left - 1)


@pytest.mark.parametrize(
    "nums,l,r,ex", [([2, 1, 4, 3], 2, 3, 3), ([2, 9, 2, 5, 6], 2, 8, 7)]
)
def test_opt(nums, l, r, ex):
    assert solve_optimal(nums, l, r) == ex

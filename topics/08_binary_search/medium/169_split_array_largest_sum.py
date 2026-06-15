"""
Problem: Split Array Largest Sum
Difficulty: Medium  Companies: Google,Facebook,Amazon
Problem Statement: Split array into k non-empty subarrays to minimize the largest sum.
Complexity: Time O(N log(sum)), Space O(1)
"""

import pytest
from typing import List


def solve_brute(nums, k):
    return solve_optimal(nums, k)


def solve_optimal(nums, k):
    def can_split(mid):
        count = 1
        curr = 0
        for n in nums:
            curr += n
            if curr > mid:
                count += 1
                curr = n
        return count <= k

    l, r = max(nums), sum(nums)
    while l < r:
        mid = (l + r) // 2
        if can_split(mid):
            r = mid
        else:
            l = mid + 1
    return l


@pytest.mark.parametrize(
    "nums,k,ex", [([7, 2, 5, 10, 8], 2, 18), ([1, 2, 3, 4, 5], 2, 9)]
)
def test_opt(nums, k, ex):
    assert solve_optimal(nums, k) == ex

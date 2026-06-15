"""
Problem: Find K-th Smallest Pair Distance
Difficulty: Hard  Companies: Google,Facebook,Amazon
Problem Statement: Return kth smallest distance among all pairs in nums.
Complexity: Time O(N log N + N log W), Space O(1)
"""

import pytest
from typing import List


def solve_brute(nums, k):
    dists = sorted(
        abs(nums[i] - nums[j])
        for i in range(len(nums))
        for j in range(i + 1, len(nums))
    )
    return dists[k - 1]


def solve_optimal(nums, k):
    nums.sort()
    n = len(nums)

    def count_pairs(mid):
        cnt = l = 0
        for r in range(n):
            while nums[r] - nums[l] > mid:
                l += 1
            cnt += r - l
        return cnt

    l, r = 0, nums[-1] - nums[0]
    while l < r:
        mid = (l + r) // 2
        if count_pairs(mid) < k:
            l = mid + 1
        else:
            r = mid
    return l


@pytest.mark.parametrize(
    "nums,k,ex", [([1, 3, 1], 1, 0), ([1, 1, 1], 2, 0), ([1, 6, 1], 3, 5)]
)
def test_opt(nums, k, ex):
    assert solve_optimal(nums, k) == ex


@pytest.mark.parametrize("nums,k,ex", [([1, 3, 1], 1, 0)])
def test_brute(nums, k, ex):
    assert solve_brute(nums, k) == ex

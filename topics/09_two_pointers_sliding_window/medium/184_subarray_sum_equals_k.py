"""
Problem: Subarray Sum Equals K
Difficulty: Medium  Companies: Meta,Amazon,Google,Microsoft
Problem Statement: Return total number of subarrays whose sum equals k.
Complexity: Time O(N), Space O(N)
"""

import pytest
from typing import List
from collections import defaultdict


def solve_brute(nums, k):
    cnt = 0
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            if s == k:
                cnt += 1
    return cnt


def solve_optimal(nums, k):
    prefix = {0: 1}
    curr = cnt = 0
    for n in nums:
        curr += n
        cnt += prefix.get(curr - k, 0)
        prefix[curr] = prefix.get(curr, 0) + 1
    return cnt


@pytest.mark.parametrize("nums,k,ex", [([1, 1, 1], 2, 2), ([1, 2, 3], 3, 2)])
def test_opt(nums, k, ex):
    assert solve_optimal(nums, k) == ex

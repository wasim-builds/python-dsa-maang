"""
Problem: Subarray Sum Equals K
Difficulty: Medium  Companies: Meta,Amazon,Google,Microsoft
Problem Statement: Return total number of subarrays whose sum equals k.
Complexity: Time O(N), Space O(N)
"""

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


if __name__ == "__main__":
    test_cases = [([1, 1, 1], 2, 2), ([1, 2, 3], 3, 2)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, k, ex in test_cases:
        assert solve_optimal(nums, k) == ex
    print("All tests passed successfully!")

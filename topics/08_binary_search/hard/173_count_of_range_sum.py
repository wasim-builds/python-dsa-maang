"""
Problem: Count of Range Sum
Difficulty: Hard  Companies: Google
Problem Statement: Count range sums that lie in [lower, upper] inclusive.
Complexity: Time O(N log N) merge sort, Space O(N)
"""

import pytest
from typing import List


def solve_brute(nums, lo, hi):
    pre = [0]
    cnt = 0
    for n in nums:
        pre.append(pre[-1] + n)
    for i in range(len(pre)):
        for j in range(i + 1, len(pre)):
            if lo <= pre[j] - pre[i] <= hi:
                cnt += 1
    return cnt


def solve_optimal(nums, lo, hi):
    pre = [0]
    for n in nums:
        pre.append(pre[-1] + n)

    def merge_count(ps):
        if len(ps) <= 1:
            return ps, 0
        mid = len(ps) // 2
        L, lc = merge_count(ps[:mid])
        R, rc = merge_count(ps[mid:])
        count = lc + rc
        j = k = 0
        for l in L:
            while j < len(R) and R[j] - l < lo:
                j += 1
            while k < len(R) and R[k] - l <= hi:
                k += 1
            count += k - j
        return sorted(L + R), count

    _, ans = merge_count(pre)
    return ans


@pytest.mark.parametrize("nums,lo,hi,ex", [([-2, 5, -1], -2, 2, 3), ([], 0, 0, 0)])
def test_opt(nums, lo, hi, ex):
    assert solve_optimal(nums, lo, hi) == ex

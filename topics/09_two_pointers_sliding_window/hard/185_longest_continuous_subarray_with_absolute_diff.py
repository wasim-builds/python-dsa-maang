"""
Problem: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Return max length subarray where max-min <= limit.
Complexity: Time O(N), Space O(N)
"""

from typing import List
from collections import deque


def solve_brute(nums, limit):
    res = 0
    for i in range(len(nums)):
        mn = mx = nums[i]
        for j in range(i, len(nums)):
            mn = min(mn, nums[j])
            mx = max(mx, nums[j])
            if mx - mn <= limit:
                res = max(res, j - i + 1)
            else:
                break
    return res


def solve_optimal(nums, limit):
    maxq = deque()
    minq = deque()
    l = res = 0
    for r, n in enumerate(nums):
        while maxq and nums[maxq[-1]] <= n:
            maxq.pop()
        while minq and nums[minq[-1]] >= n:
            minq.pop()
        maxq.append(r)
        minq.append(r)
        while nums[maxq[0]] - nums[minq[0]] > limit:
            l += 1
            if maxq[0] < l:
                maxq.popleft()
            if minq[0] < l:
                minq.popleft()
        res = max(res, r - l + 1)
    return res


if __name__ == "__main__":
    test_cases = [
        ([8, 2, 4, 7], 4, 2),
        ([10, 1, 2, 4, 7, 2], 5, 4),
        ([4, 2, 2, 2, 4, 4, 2, 2], 0, 3),
    ]

    for nums, limit, ex in test_cases:
        assert solve_optimal(nums, limit) == ex
    print("All tests passed successfully!")

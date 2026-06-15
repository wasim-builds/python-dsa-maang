"""
Problem: Sliding Window Maximum
Difficulty: Hard
Topic: 01_arrays  Companies: Amazon,Google,Meta,Bloomberg
Problem Statement: Given array nums and window size k, return max of each window.
Complexity: Time O(N), Space O(k)
"""

from typing import List
from collections import deque


def solve_brute(nums, k):
    return [max(nums[i : i + k]) for i in range(len(nums) - k + 1)]


def solve_optimal(nums, k):
    q = deque()
    res = []
    for i, n in enumerate(nums):
        while q and nums[q[-1]] <= n:
            q.pop()
        q.append(i)
        if q[0] == i - k:
            q.popleft()
        if i >= k - 1:
            res.append(nums[q[0]])
    return res


if __name__ == "__main__":
    test_cases = [([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7])]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, k, ex in test_cases:
        assert solve_brute(nums, k) == ex
    print("All tests passed successfully!")

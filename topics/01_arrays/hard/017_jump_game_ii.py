"""
Problem: Jump Game II
Difficulty: Hard
Topic: 01_arrays  Companies: Amazon,Google,Microsoft,Uber
Problem Statement: Return minimum jumps to reach last index. You can jump up to nums[i] steps from position i.
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(nums):
    dp = [float("inf")] * len(nums)
    dp[0] = 0
    for i in range(len(nums)):
        for j in range(1, nums[i] + 1):
            if i + j < len(nums):
                dp[i + j] = min(dp[i + j], dp[i] + 1)
    return dp[-1]


def solve_optimal(nums):
    jumps = curr_end = curr_far = 0
    for i in range(len(nums) - 1):
        curr_far = max(curr_far, i + nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = curr_far
    return jumps


if __name__ == "__main__":
    test_cases = [([2, 3, 1, 1, 4], 2)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, ex in test_cases:
        assert solve_brute(nums) == ex
    print("All tests passed successfully!")

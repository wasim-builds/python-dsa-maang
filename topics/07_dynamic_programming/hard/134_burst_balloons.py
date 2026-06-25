"""
Problem: Burst Balloons
Difficulty: Hard  Companies: Google,Amazon,Facebook
Problem Statement: Burst all balloons to get max coins. nums[left]*nums[i]*nums[right] for each burst.
Complexity: Time O(N^3), Space O(N^2)
"""

from typing import List


def solve_brute(nums):
    return solve_optimal(nums)


def solve_optimal(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for l in range(0, n - length):
            r = l + length
            for k in range(l + 1, r):
                dp[l][r] = max(
                    dp[l][r], nums[l] * nums[k] * nums[r] + dp[l][k] + dp[k][r]
                )
    return dp[0][n - 1]


if __name__ == "__main__":
    test_cases = [([3, 1, 5, 8], 167), ([1, 5], 10)]

    for nums, ex in test_cases:
        assert solve_optimal(nums) == ex
    print("All tests passed successfully!")

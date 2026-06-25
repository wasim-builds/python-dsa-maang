"""
Problem: Coin Change
Difficulty: Medium
Topic: 07_dynamic_programming
Companies: Amazon, Microsoft, Bloomberg, Meta, Google

Problem Statement:
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.
You may assume that you have an infinite number of each kind of coin.

Complexity Proof:
- Time Complexity: O(A * C) where A is the amount and C is the number of coins. For every amount up to A, we loop through all C coins to find the minimum.
- Space Complexity: O(A) to store the DP array of size `amount + 1`.
"""

from typing import List


# BRUTE FORCE (Recursive DFS with no memoization)
# Time: O(C^A), Space: O(A)
def solve_brute(coins: List[int], amount: int) -> int:
    def dfs(rem):
        if rem < 0:
            return -1
        if rem == 0:
            return 0

        min_cost = float("inf")
        for coin in coins:
            res = dfs(rem - coin)
            if res != -1:
                min_cost = min(min_cost, res + 1)

        return min_cost if min_cost != float("inf") else -1

    return dfs(amount)


# OPTIMAL (Bottom-Up DP)
# Time: O(A * C), Space: O(A)
def solve_optimal(coins: List[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != float("inf") else -1


# Note: Only testing brute force on small amounts to prevent timeout

if __name__ == "__main__":
    test_cases = [([1, 2, 5], 11, 3), ([2], 3, -1), ([1], 0, 0)]

    for coins, amount, expected in test_cases:
        assert solve_brute(coins, amount) == expected
    print("All tests passed successfully!")

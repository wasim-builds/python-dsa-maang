"""
Problem: Min Cost Climbing Stairs
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Pay cost[i] to climb stair. Can climb 1 or 2 steps. Find min cost to top.
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]


def solve_optimal(cost):
    a = b = 0
    for i in range(2, len(cost) + 1):
        a, b = b, min(b + cost[i - 1], a + cost[i - 2])
    return b


if __name__ == "__main__":
    test_cases = [([10, 15, 20], 15), ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)]

    for c, ex in test_cases:
        assert solve_optimal(c) == ex
    print("All tests passed successfully!")

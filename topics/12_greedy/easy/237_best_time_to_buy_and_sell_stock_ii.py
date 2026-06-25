"""
Problem: Best Time to Buy and Sell Stock II
Difficulty: Easy  Companies: Amazon,Google,Bloomberg,Microsoft
Problem Statement: Maximize profit buying/selling on any day (unlimited transactions).
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(prices):
    return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


def solve_optimal(prices):
    return solve_brute(prices)


if __name__ == "__main__":
    test_cases = [([7, 1, 5, 3, 6, 4], 7), ([1, 2, 3, 4, 5], 4), ([7, 6, 4, 3, 1], 0)]

    for p, ex in test_cases:
        assert solve_optimal(p) == ex
    print("All tests passed successfully!")

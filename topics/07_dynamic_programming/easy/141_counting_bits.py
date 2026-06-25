"""
Problem: Counting Bits
Difficulty: Easy  Companies: Amazon,Microsoft,Google,Facebook
Problem Statement: Return array of length n+1 where ans[i] is number of 1 bits in i.
Complexity: Time O(N), Space O(N)
"""

from typing import List


def solve_brute(n):
    return [bin(i).count("1") for i in range(n + 1)]


def solve_optimal(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp


if __name__ == "__main__":
    test_cases = [(2, [0, 1, 1]), (5, [0, 1, 1, 2, 1, 2])]

    for n, ex in test_cases:
        assert solve_optimal(n) == ex
    print("All tests passed successfully!")

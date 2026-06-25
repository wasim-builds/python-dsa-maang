"""
Problem: Gray Code
Difficulty: Medium  Companies: Amazon,Google,Microsoft
Problem Statement: Return gray code sequence of n bits.
Complexity: Time O(2^N), Space O(2^N)
"""

from typing import List


def solve_brute(n):
    return solve_optimal(n)


def solve_optimal(n):
    return [i ^ (i >> 1) for i in range(1 << n)]


if __name__ == "__main__":
    test_cases = [(2, [0, 1, 3, 2]), (1, [0, 1])]

    for n, ex in test_cases:
        assert solve_optimal(n) == ex
    print("All tests passed successfully!")

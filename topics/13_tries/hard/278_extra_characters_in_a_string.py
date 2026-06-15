"""
Problem: Extra Characters in a String
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Break string using words from dictionary. Return min extra characters left over.
Complexity: Time O(N^2 + W * L), Space O(N + W * L)
"""

from typing import List


def solve_brute(s, dictionary):
    return solve_optimal(s, dictionary)


def solve_optimal(s, dictionary):
    wordset = set(dictionary)
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(i):
            if s[j:i] in wordset:
                dp[i] = min(dp[i], dp[j])
    return dp[n]


if __name__ == "__main__":
    test_cases = [
        ("leetscode", ["leet", "code", "leetcode"], 1),
        ("sayhelloworld", ["hello", "world"], 3),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s, d, ex in test_cases:
        assert solve_optimal(s, d) == ex
    print("All tests passed successfully!")

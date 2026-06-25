"""
Problem: Concatenated Words
Difficulty: Hard  Companies: Google,Amazon,Facebook,Pinterest
Problem Statement: Return all words that can be formed by concatenating other words.
Complexity: Time O(N * L^2), Space O(N * L)
"""

from typing import List


def solve_brute(words):
    return solve_optimal(words)


def solve_optimal(words):
    wordset = set(words)
    res = []

    def can_form(w):
        if not w:
            return False
        dp = [False] * (len(w) + 1)
        dp[0] = True
        for i in range(1, len(w) + 1):
            for j in range(i):
                if dp[j] and w[j:i] in wordset and (j > 0 or w[j:i] != w):
                    dp[i] = True
                    break
        return dp[len(w)]

    return [w for w in words if can_form(w)]


if __name__ == "__main__":
    test_cases = [
        (
            [
                "cat",
                "cats",
                "catsdogcats",
                "dog",
                "dogcatsdog",
                "hippopotamuses",
                "rat",
                "ratcatdogcat",
            ],
            ["catsdogcats", "dogcatsdog", "ratcatdogcat"],
        )
    ]

    for w, ex in test_cases:
        assert sorted(solve_optimal(w)) == sorted(ex)
    print("All tests passed successfully!")

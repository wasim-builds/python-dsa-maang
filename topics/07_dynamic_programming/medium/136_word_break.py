"""
Problem: Word Break
Difficulty: Medium
Topic: 07_dynamic_programming
Companies: Amazon, Google, Meta, Microsoft, Bloomberg

Problem Statement:
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Complexity Proof:
- Time Complexity: O(N * M * L) where N is the length of `s`, M is the number of words in `wordDict`, and L is the maximum length of a word in `wordDict`. For each of the N characters, we check up to M words, which takes O(L) time to compare.
- Space Complexity: O(N) for the DP array of size N + 1.
"""

from typing import List


# OPTIMAL (Bottom-Up DP)
# Time: O(N * M * L), Space: O(N)
def solve_optimal(s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True  # Base case: empty string at the end is valid

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            # If there's enough characters left in s to match w
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                # dp[i] becomes True if the rest of the string starting from i + len(w) can also be segmented
                dp[i] = dp[i + len(w)]
            
            # If we found a valid match that allows segmenting the rest, 
            # no need to check other words for this index `i`.
            if dp[i]:
                break

    return dp[0]


# BRUTE FORCE / ALTERNATIVE (Top-Down DFS with Memoization)
# Time: O(N^3) depending on slicing and dict checks, Space: O(N)
def solve_brute(s: str, wordDict: List[str]) -> bool:
    wordSet = set(wordDict)
    memo = {}

    def dfs(i):
        # i represents the starting index of the substring we are currently checking
        if i == len(s):
            return True
        if i in memo:
            return memo[i]

        for j in range(i + 1, len(s) + 1):
            if s[i:j] in wordSet and dfs(j):
                memo[i] = True
                return True

        memo[i] = False
        return False

    return dfs(0)


if __name__ == "__main__":
    test_cases = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ]

    for s, wordDict, expected in test_cases:
        assert solve_optimal(s, wordDict) == expected
        assert solve_brute(s, wordDict) == expected
    print("All tests passed successfully!")

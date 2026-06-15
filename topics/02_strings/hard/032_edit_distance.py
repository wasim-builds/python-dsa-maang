"""
Problem: Edit Distance
Difficulty: Hard
Topic: 02_strings  Companies: Google,Amazon,Microsoft,Bloomberg,Meta
Problem Statement: Given two strings word1 and word2, return minimum operations (insert/delete/replace) to convert word1 to word2.
Complexity: Time O(M*N), Space O(M*N) DP
"""


def solve_brute(word1, word2):
    from functools import lru_cache

    @lru_cache(None)
    def dp(i, j):
        if i == 0:
            return j
        if j == 0:
            return i
        if word1[i - 1] == word2[j - 1]:
            return dp(i - 1, j - 1)
        return 1 + min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1))

    return dp(len(word1), len(word2))


def solve_optimal(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]


if __name__ == "__main__":
    test_cases = [("horse", "ros", 3)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for w1, w2, ex in test_cases:
        assert solve_brute(w1, w2) == ex
    print("All tests passed successfully!")

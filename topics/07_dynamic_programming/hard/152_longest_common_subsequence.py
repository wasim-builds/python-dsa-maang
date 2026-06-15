"""
Problem: Longest Common Subsequence
Difficulty: Hard  Companies: Amazon,Google,Microsoft,Bloomberg
Problem Statement: Return length of longest common subsequence of text1 and text2.
Complexity: Time O(M*N), Space O(min(M,N))
"""


def solve_brute(t1, t2):
    from functools import lru_cache

    @lru_cache(None)
    def dp(i, j):
        if i == len(t1) or j == len(t2):
            return 0
        if t1[i] == t2[j]:
            return 1 + dp(i + 1, j + 1)
        return max(dp(i + 1, j), dp(i, j + 1))

    return dp(0, 0)


def solve_optimal(t1, t2):
    m, n = len(t1), len(t2)
    if m < n:
        t1, t2 = t2, t1
        m, n = n, m
    dp = [0] * (n + 1)
    for c in t1:
        prev = 0
        for j in range(1, n + 1):
            tmp = dp[j]
            dp[j] = prev + 1 if c == t2[j - 1] else max(dp[j], dp[j - 1])
            prev = tmp
    return dp[n]


if __name__ == "__main__":
    test_cases = [("abcde", "ace", 3), ("abc", "abc", 3), ("abc", "def", 0)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for t1, t2, ex in test_cases:
        assert solve_optimal(t1, t2) == ex
    print("All tests passed successfully!")

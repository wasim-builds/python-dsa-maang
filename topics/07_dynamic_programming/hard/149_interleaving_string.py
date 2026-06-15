"""
Problem: Interleaving String
Difficulty: Hard  Companies: Google,Amazon,Microsoft
Problem Statement: Given s1,s2,s3, check if s3 is formed by interleaving s1 and s2.
Complexity: Time O(M*N), Space O(N)
"""


def solve_brute(s1, s2, s3):
    from functools import lru_cache

    @lru_cache(None)
    def dp(i, j):
        if i + j == len(s3):
            return True
        if i < len(s1) and s1[i] == s3[i + j] and dp(i + 1, j):
            return True
        if j < len(s2) and s2[j] == s3[i + j] and dp(i, j + 1):
            return True
        return False

    return len(s1) + len(s2) == len(s3) and dp(0, 0)


def solve_optimal(s1, s2, s3):
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False
    dp = [False] * (n + 1)
    dp[0] = True
    for j in range(1, n + 1):
        dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
    for i in range(1, m + 1):
        dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (
                dp[j - 1] and s2[j - 1] == s3[i + j - 1]
            )
    return dp[n]


if __name__ == "__main__":
    test_cases = [
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s1, s2, s3, ex in test_cases:
        assert solve_optimal(s1, s2, s3) == ex
    print("All tests passed successfully!")

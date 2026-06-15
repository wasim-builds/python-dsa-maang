"""
Problem: Palindrome Partitioning II
Difficulty: Hard  Companies: Google,Amazon,Microsoft
Problem Statement: Return minimum cuts needed for a palindrome partitioning of s.
Complexity: Time O(N^2), Space O(N^2)
"""


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    n = len(s)
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        for l in range(i + 1):
            if s[l] == s[i] and (i - l <= 2 or is_pal[l + 1][i - 1]):
                is_pal[l][i] = True
    dp = [float("inf")] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0
            continue
        for j in range(1, i + 1):
            if is_pal[j][i]:
                dp[i] = min(dp[i], dp[j - 1] + 1)
    return dp[n - 1]


if __name__ == "__main__":
    test_cases = [("aab", 1), ("a", 0), ("ab", 1)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s, ex in test_cases:
        assert solve_optimal(s) == ex
    print("All tests passed successfully!")

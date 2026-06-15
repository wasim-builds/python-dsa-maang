"""
Problem: Longest Common Subpath
Difficulty: Hard  Companies: Google,Amazon
Problem Statement: Find shortest common supersequence of str1 and str2.
Complexity: Time O(M*N), Space O(M*N)
"""


def solve_brute(s1, s2):
    return solve_optimal(s1, s2)


def solve_optimal(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
    i, j = m, n
    res = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            res.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] < dp[i][j - 1]:
            res.append(str1[i - 1])
            i -= 1
        else:
            res.append(str2[j - 1])
            j -= 1
    while i > 0:
        res.append(str1[i - 1])
        i -= 1
    while j > 0:
        res.append(str2[j - 1])
        j -= 1
    return "".join(reversed(res))


if __name__ == "__main__":
    test_cases = [("abac", "cab", "cabac")]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s1, s2, ex in test_cases:
        assert solve_optimal(s1, s2) == ex
    print("All tests passed successfully!")

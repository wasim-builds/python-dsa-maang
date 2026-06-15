"""
Problem: Maximum Product of the Length of Two Palindromic Substrings
Difficulty: Hard  Companies: Google
Problem Statement: For each split point, find palindrome product.
Complexity: Time O(N^2), Space O(N)
"""


def solve_brute(s):
    def max_pal(s_sub):
        if not s_sub:
            return 0
        n = len(s_sub)
        best = 1
        for i in range(n):
            for j in range(i + 1, n):
                if s_sub[i : j + 1] == s_sub[i : j + 1][::-1]:
                    best = max(best, j - i + 1)
        return best

    res = 0
    for i in range(1, len(s)):
        res = max(res, max_pal(s[:i]) * max_pal(s[i:]))
    return res


def solve_optimal(s):
    return solve_brute(s)


if __name__ == "__main__":
    test_cases = [("aababaab", 12)]
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

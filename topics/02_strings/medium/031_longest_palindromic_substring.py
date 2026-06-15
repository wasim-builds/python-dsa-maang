"""
Problem: Longest Palindromic Substring
Difficulty: Medium
Topic: 02_strings
Companies: Amazon, Microsoft, Meta, Google, Apple

Problem Statement:
Given a string `s`, return the longest palindromic substring in `s`.

Complexity Proof:
- Time Complexity: O(N^2) because we expand around the center for each of the N characters. The expansion takes O(N) time in the worst case.
- Space Complexity: O(1) because we only keep track of indices (`resLen`, `res`). Note: extracting the final string slice takes O(N) memory but is considered O(1) extra space.
"""


# BRUTE FORCE
# Time: O(N^3), Space: O(1)
def solve_brute(s: str) -> str:
    res = ""
    resLen = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i : j + 1]
            if sub == sub[::-1] and len(sub) > resLen:
                res = sub
                resLen = len(sub)

    return res


# OPTIMAL (Expand Around Center)
# Time: O(N^2), Space: O(1)
def solve_optimal(s: str) -> str:
    res = ""
    resLen = 0

    for i in range(len(s)):
        # Odd length palindromes
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

        # Even length palindromes
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

    return res


if __name__ == "__main__":
    test_cases = [
        ("babad", ["bab", "aba"]),
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s, expected_options in test_cases:
        assert solve_brute(s) in expected_options
    print("All tests passed successfully!")

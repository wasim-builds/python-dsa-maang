"""
Problem: Valid Palindrome
Difficulty: Easy
Topic: 02_strings
Companies: Meta, Amazon, Microsoft, Apple, Spotify

Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

Complexity Proof:
- Time Complexity: O(N) where N is the length of the string. The two pointers traverse the string at most once.
- Space Complexity: O(1) because we do not allocate any extra memory. We just use two pointers.
"""

import re


# BRUTE FORCE
# Time: O(N), Space: O(N)
def solve_brute(s: str) -> bool:
    new_str = ""
    for c in s:
        if c.isalnum():
            new_str += c.lower()
    return new_str == new_str[::-1]


# OPTIMAL
# Time: O(N), Space: O(1)
def solve_optimal(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l, r = l + 1, r - 1

    return True


def alphaNum(c):
    return (
        ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9")
    )


if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for input_data, expected in test_cases:
        assert solve_brute(input_data) == expected
    print("All tests passed successfully!")

"""
Problem: Reverse String
Difficulty: Easy
Topic: 02_strings  Companies: Amazon,Google,Microsoft
Problem Statement: Write a function that reverses a string in-place. Input is char array.
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(s):
    s[:] = s[::-1]


def solve_optimal(s):
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1


if __name__ == "__main__":
    test_cases = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s, ex in test_cases:
        solve_optimal(s)
        assert s == ex
    print("All tests passed successfully!")

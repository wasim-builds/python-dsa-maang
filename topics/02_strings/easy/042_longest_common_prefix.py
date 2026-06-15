"""
Problem: Longest Common Prefix
Difficulty: Easy
Topic: 02_strings  Companies: Amazon,Google,Microsoft
Problem Statement: Write a function to find the longest common prefix string amongst an array of strings.
Complexity: Time O(S) where S is sum of all chars, Space O(1)
"""

from typing import List


def solve_brute(strs):
    if not strs:
        return ""
    pref = strs[0]
    for s in strs[1:]:
        while not s.startswith(pref):
            pref = pref[:-1]
    return pref


def solve_optimal(strs):
    if not strs:
        return ""
    for i, c in enumerate(strs[0]):
        for s in strs[1:]:
            if i == len(s) or s[i] != c:
                return strs[0][:i]
    return strs[0]


if __name__ == "__main__":
    test_cases = [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], "")]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for strs, ex in test_cases:
        assert solve_optimal(strs) == ex
    print("All tests passed successfully!")

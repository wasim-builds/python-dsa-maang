"""
Problem: First Unique Character in a String
Difficulty: Easy
Topic: 02_strings  Companies: Amazon,Bloomberg,Microsoft,Google
Problem Statement: Given string s, find first non-repeating character and return its index. Return -1 if none.
Complexity: Time O(N), Space O(1) since at most 26 keys
"""

from collections import Counter


def solve_brute(s):
    for i, c in enumerate(s):
        if s.count(c) == 1:
            return i
    return -1


def solve_optimal(s):
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1


if __name__ == "__main__":
    test_cases = [("leetcode", 0), ("loveleetcode", 2), ("aabb", -1)]
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

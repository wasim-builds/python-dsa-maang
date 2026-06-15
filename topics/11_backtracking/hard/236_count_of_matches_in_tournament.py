"""
Problem: Maximum Length of a Concatenated String with Unique Characters
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Given array of strings, find max length of concatenation with unique characters.
Complexity: Time O(2^N * N), Space O(N)
"""

from typing import List


def solve_brute(arr):
    return solve_optimal(arr)


def solve_optimal(arr):
    res = [0]

    def bt(idx, chars):
        res[0] = max(res[0], len(chars))
        for i in range(idx, len(arr)):
            w = arr[i]
            if len(set(w)) < len(w):
                continue
            if not set(w) & chars:
                bt(i + 1, chars | set(w))

    bt(0, set())
    return res[0]


if __name__ == "__main__":
    test_cases = [
        (["un", "iq", "ue"], 4),
        (["cha", "r", "act", "ers"], 6),
        (["abcdefghijklmnopqrstuvwxyz"], 26),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arr, ex in test_cases:
        assert solve_optimal(arr) == ex
    print("All tests passed successfully!")

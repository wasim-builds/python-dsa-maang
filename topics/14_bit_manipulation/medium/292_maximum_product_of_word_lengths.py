"""
Problem: Maximum Product of Word Lengths
Difficulty: Medium  Companies: Amazon,Google
Problem Statement: Return max product of lengths of two words that share no common letters.
Complexity: Time O(N^2), Space O(N) bitmask
"""

from typing import List


def solve_brute(words):
    return solve_optimal(words)


def solve_optimal(words):
    masks = [0] * len(words)
    for i, w in enumerate(words):
        for c in w:
            masks[i] |= 1 << (ord(c) - ord("a"))
    res = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if not (masks[i] & masks[j]):
                res = max(res, len(words[i]) * len(words[j]))
    return res


if __name__ == "__main__":
    test_cases = [
        (["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], 16),
        (["a", "ab", "abc", "d", "cd", "bcd", "abcd"], 4),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for w, ex in test_cases:
        assert solve_optimal(w) == ex
    print("All tests passed successfully!")

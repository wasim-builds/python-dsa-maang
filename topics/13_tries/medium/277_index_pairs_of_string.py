"""
Problem: Index Pairs of a String
Difficulty: Medium  Companies: Amazon,Google
Problem Statement: Find all index pairs [i,j] where text[i..j] is a word in words.
Complexity: Time O(N * L), Space O(N * L)
"""

from typing import List


def solve_brute(text, words):
    return sorted(
        [i, i + len(w) - 1]
        for w in words
        for i in range(len(text))
        if text[i : i + len(w)] == w
    )


def solve_optimal(text, words):
    return solve_brute(text, words)


if __name__ == "__main__":
    test_cases = [
        (
            "thestoryofleetcodeandme",
            ["story", "fleet", "leetcode"],
            [[3, 7], [9, 13], [10, 17]],
        ),
        ("ababa", ["aba", "ab"], [[0, 1], [0, 2], [2, 3], [2, 4]]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for t, w, ex in test_cases:
        assert solve_optimal(t, w) == ex
    print("All tests passed successfully!")

"""
Problem: Index Pairs of a String
Difficulty: Medium  Companies: Amazon,Google
Problem Statement: Find all index pairs [i,j] where text[i..j] is a word in words.
Complexity: Time O(N * L), Space O(N * L)
"""

import pytest
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


@pytest.mark.parametrize(
    "t,w,ex",
    [
        (
            "thestoryofleetcodeandme",
            ["story", "fleet", "leetcode"],
            [[3, 7], [9, 13], [10, 17]],
        ),
        ("ababa", ["aba", "ab"], [[0, 1], [0, 2], [2, 3], [2, 4]]),
    ],
)
def test_opt(t, w, ex):
    assert solve_optimal(t, w) == ex

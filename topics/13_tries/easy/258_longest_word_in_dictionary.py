"""
Problem: Longest Word in Dictionary
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Return longest word in words that can be built one char at a time.
Complexity: Time O(N * M), Space O(N * M)
"""

import pytest
from typing import List


def solve_brute(words):
    return solve_optimal(words)


def solve_optimal(words):
    wordset = set(words)
    words.sort(key=lambda x: (-len(x), x))
    for w in words:
        if all(w[:i] in wordset for i in range(1, len(w))):
            return w
    return ""


@pytest.mark.parametrize(
    "w,ex",
    [
        (["w", "wo", "wor", "worl", "world"], "world"),
        (["a", "banana", "app", "appl", "ap", "apply", "apple"], "apple"),
    ],
)
def test_opt(w, ex):
    assert solve_optimal(w) == ex

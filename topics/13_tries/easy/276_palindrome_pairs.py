"""
Problem: Palindrome Pairs
Difficulty: Easy  Companies: Google,Amazon,Airbnb
Problem Statement: Given list of unique words, find all pairs (i,j) where words[i]+words[j] is palindrome.
Complexity: Time O(N * K^2), Space O(N * K)
"""

import pytest
from typing import List


def solve_brute(words):
    return solve_optimal(words)


def solve_optimal(words):
    lookup = {w: i for i, w in enumerate(words)}
    res = []

    def is_pal(s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    for i, w in enumerate(words):
        for j in range(len(w) + 1):
            prefix = w[:j]
            suffix = w[j:]
            if is_pal(prefix, 0, len(prefix) - 1):
                rev = suffix[::-1]
                if rev in lookup and lookup[rev] != i:
                    res.append([lookup[rev], i])
            if j > 0 and is_pal(suffix, 0, len(suffix) - 1):
                rev = prefix[::-1]
                if rev in lookup and lookup[rev] != i:
                    res.append([i, lookup[rev]])
    return [list(x) for x in set(tuple(x) for x in res)]


@pytest.mark.parametrize(
    "w,ex", [(["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]])]
)
def test_opt(w, ex):
    assert sorted(solve_optimal(w)) == sorted(ex)

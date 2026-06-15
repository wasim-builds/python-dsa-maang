"""
Problem: Prefix and Suffix Search
Difficulty: Medium  Companies: Google,Amazon
Problem Statement: Given list of words, find index of word with given prefix and suffix. Return highest.
Complexity: Time O(N * L^2) build, O(P + S) search; Space O(N * L^2)
"""

import pytest
from typing import List


class WordFilter:
    def __init__(self, words):
        self.lookup = {}
        for idx, w in enumerate(words):
            n = len(w)
            for i in range(n + 1):
                for j in range(n + 1):
                    self.lookup[(w[:i], w[j:])] = idx

    def f(self, pref, suff):
        return self.lookup.get((pref, suff), -1)


def test_word_filter():
    wf = WordFilter(["apple"])
    assert wf.f("a", "e") == 0
    assert wf.f("b", "") == -1

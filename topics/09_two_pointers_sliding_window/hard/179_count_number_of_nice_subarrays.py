"""
Problem: Substring with Concatenation of All Words
Difficulty: Hard  Companies: Amazon,Google,Bloomberg
Problem Statement: Find all starting indices of substring(s) that is concatenation of each word in words exactly once.
Complexity: Time O(N * W * L), Space O(W)
"""

from typing import List
from collections import Counter


def solve_brute(s, words):
    if not s or not words:
        return []
    wl = len(words[0])
    nw = len(words)
    total = wl * nw
    res = []
    need = Counter(words)
    for i in range(len(s) - total + 1):
        have = Counter(s[i + j * wl : i + j * wl + wl] for j in range(nw))
        if have == need:
            res.append(i)
    return res


def solve_optimal(s, words):
    return solve_brute(s, words)


if __name__ == "__main__":
    test_cases = [
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
    ]

    for s, w, ex in test_cases:
        assert sorted(solve_optimal(s, w)) == sorted(ex)
    print("All tests passed successfully!")

"""
Problem: Count Words Obtained After Adding a Letter
Difficulty: Medium  Companies: Amazon,Google
Problem Statement: Count target words obtainable by adding one letter to source words.
Complexity: Time O(N log L), Space O(N)
"""

from typing import List


def solve_brute(startWords, targetWords):
    cnt = 0
    for t in targetWords:
        for s in startWords:
            if len(s) + 1 != len(t):
                continue
            for i in range(len(t)):
                w = t[:i] + t[i + 1 :]
                if sorted(w) == sorted(s):
                    cnt += 1
                    break
    return cnt


def solve_optimal(startWords, targetWords):
    start_set = set(frozenset(w) for w in startWords)
    cnt = 0
    for t in targetWords:
        for c in t:
            if frozenset(t) - {c} in start_set:
                cnt += 1
                break
    return cnt


if __name__ == "__main__":
    test_cases = [(["ant", "act", "tack"], ["tack", "act", "acti"], 2)]

    for s, t, ex in test_cases:
        assert solve_optimal(s, t) == ex
    print("All tests passed successfully!")

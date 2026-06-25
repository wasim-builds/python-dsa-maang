"""
Problem: Permutation in String
Difficulty: Medium  Companies: Microsoft,Amazon,Facebook
Problem Statement: Return true if s2 contains a permutation of s1.
Complexity: Time O(N), Space O(1)
"""

from collections import Counter


def solve_brute(s1, s2):
    c1 = Counter(s1)
    n = len(s1)
    for i in range(len(s2) - n + 1):
        if Counter(s2[i : i + n]) == c1:
            return True
    return False


def solve_optimal(s1, s2):
    if len(s1) > len(s2):
        return False
    need = Counter(s1)
    have = Counter(s2[: len(s1)])
    if need == have:
        return True
    for i in range(len(s1), len(s2)):
        have[s2[i]] += 1
        left = s2[i - len(s1)]
        have[left] -= 1
        if have[left] == 0:
            del have[left]
        if have == need:
            return True
    return False


if __name__ == "__main__":
    test_cases = [("ab", "eidbaooo", True), ("ab", "eidboaoo", False)]

    for s1, s2, ex in test_cases:
        assert solve_optimal(s1, s2) == ex
    print("All tests passed successfully!")

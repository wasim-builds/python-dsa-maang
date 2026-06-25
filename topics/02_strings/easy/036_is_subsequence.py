"""
Problem: Is Subsequence
Difficulty: Easy
Topic: 02_strings  Companies: Google,Amazon,Microsoft,Uber
Problem Statement: Given strings s and t, return true if s is a subsequence of t.
Complexity: Time O(N), Space O(1)
"""


def solve_brute(s, t):
    it = iter(t)
    return all(c in it for c in s)


def solve_optimal(s, t):
    i = 0
    for c in t:
        if i < len(s) and c == s[i]:
            i += 1
    return i == len(s)


if __name__ == "__main__":
    test_cases = [("ace", "abcde", True), ("aec", "abcde", False), ("", "abc", True)]

    for s, t, ex in test_cases:
        assert solve_optimal(s, t) == ex
    print("All tests passed successfully!")

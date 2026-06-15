"""
Problem: Palindrome Partitioning
Difficulty: Easy  Companies: Amazon,Google,Microsoft,Meta
Problem Statement: Partition s so every substring is a palindrome. Return all partitions.
Complexity: Time O(N * 2^N), Space O(N^2)
"""

from typing import List


def is_pal(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    res = []

    def bt(start, part):
        if start == len(s):
            res.append(part[:])
            return
        for end in range(start + 1, len(s) + 1):
            if is_pal(s, start, end - 1):
                part.append(s[start:end])
                bt(end, part)
                part.pop()

    bt(0, [])
    return res


if __name__ == "__main__":
    test_cases = [("aab", [["a", "a", "b"], ["aa", "b"]]), ("a", [["a"]])]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s, ex in test_cases:
        assert sorted(solve_optimal(s)) == sorted(ex)
    print("All tests passed successfully!")

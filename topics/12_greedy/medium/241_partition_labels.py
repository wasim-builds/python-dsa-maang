"""
Problem: Partition Labels
Difficulty: Medium  Companies: Amazon,Google,Facebook,Bloomberg
Problem Statement: Partition string so each letter appears in at most one part. Return sizes of partitions.
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    last = {c: i for i, c in enumerate(s)}
    res = []
    start = end = 0
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            res.append(end - start + 1)
            start = i + 1
    return res


if __name__ == "__main__":
    test_cases = [("ababcbacadefegdehijhklij", [9, 7, 8]), ("eccbbbbdec", [10])]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s, ex in test_cases:
        assert solve_optimal(s) == ex
    print("All tests passed successfully!")

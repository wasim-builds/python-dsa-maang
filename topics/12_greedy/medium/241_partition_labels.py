"""
Problem: Partition Labels
Difficulty: Medium  Companies: Amazon,Google,Facebook,Bloomberg
Problem Statement: Partition string so each letter appears in at most one part. Return sizes of partitions.
Complexity: Time O(N), Space O(1)
"""

import pytest
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


@pytest.mark.parametrize(
    "s,ex", [("ababcbacadefegdehijhklij", [9, 7, 8]), ("eccbbbbdec", [10])]
)
def test_opt(s, ex):
    assert solve_optimal(s) == ex

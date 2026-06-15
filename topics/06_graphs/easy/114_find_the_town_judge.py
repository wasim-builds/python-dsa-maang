"""
Problem: Find the Town Judge
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Find person trusted by everyone else but trusts nobody. Return -1 if not found.
Complexity: Time O(E), Space O(N)
"""

import pytest
from typing import List


def solve_brute(n, trust):
    for candidate in range(1, n + 1):
        if all(a != candidate for a, b in trust) and all(
            b == candidate for a, b in trust if a != candidate
        ):
            if sum(1 for a, b in trust if b == candidate) == n - 1:
                return candidate
    return -1


def solve_optimal(n, trust):
    score = [0] * (n + 1)
    for a, b in trust:
        score[a] -= 1
        score[b] += 1
    for i in range(1, n + 1):
        if score[i] == n - 1:
            return i
    return -1


@pytest.mark.parametrize(
    "n,t,ex",
    [(2, [[1, 2]], 2), (3, [[1, 3], [2, 3]], 3), (3, [[1, 3], [2, 3], [3, 1]], -1)],
)
def test_opt(n, t, ex):
    assert solve_optimal(n, t) == ex

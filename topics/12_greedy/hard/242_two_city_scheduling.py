"""
Problem: Two City Scheduling
Difficulty: Hard  Companies: Amazon,Google,Facebook
Problem Statement: Send n people to city A and n to city B. Minimize cost.
Complexity: Time O(N log N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(costs):
    return solve_optimal(costs)


def solve_optimal(costs):
    costs.sort(key=lambda x: x[0] - x[1])
    n = len(costs) // 2
    return sum(c[0] for c in costs[:n]) + sum(c[1] for c in costs[n:])


@pytest.mark.parametrize(
    "c,ex",
    [
        ([[10, 20], [30, 200], [400, 50], [30, 20]], 110),
        ([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]], 1859),
    ],
)
def test_opt(c, ex):
    assert solve_optimal(c) == ex

"""
Problem: Two City Scheduling
Difficulty: Hard  Companies: Amazon,Google,Facebook
Problem Statement: Send n people to city A and n to city B. Minimize cost.
Complexity: Time O(N log N), Space O(1)
"""

from typing import List


def solve_brute(costs):
    return solve_optimal(costs)


def solve_optimal(costs):
    costs.sort(key=lambda x: x[0] - x[1])
    n = len(costs) // 2
    return sum(c[0] for c in costs[:n]) + sum(c[1] for c in costs[n:])


if __name__ == "__main__":
    test_cases = [
        ([[10, 20], [30, 200], [400, 50], [30, 20]], 110),
        ([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]], 1859),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for c, ex in test_cases:
        assert solve_optimal(c) == ex
    print("All tests passed successfully!")

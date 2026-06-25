"""
Problem: Gas Station
Difficulty: Medium  Companies: Amazon,Google,Microsoft,Meta
Problem Statement: Find starting gas station to complete circular route, or -1.
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(gas, cost):
    for i in range(len(gas)):
        tank = 0
        ok = True
        for j in range(len(gas)):
            idx = (i + j) % len(gas)
            tank += gas[idx] - cost[idx]
            if tank < 0:
                ok = False
                break
        if ok:
            return i
    return -1


def solve_optimal(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    tank = start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3), ([2, 3, 4], [3, 4, 3], -1)]

    for g, c, ex in test_cases:
        assert solve_optimal(g, c) == ex
    print("All tests passed successfully!")

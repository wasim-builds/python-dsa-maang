"""
Problem: Minimum Number of Refueling Stops
Difficulty: Hard  Companies: Amazon,Google,Uber
Problem Statement: Return min stops needed to reach target. Greedy with max heap.
Complexity: Time O(N log N), Space O(N)
"""

import pytest, heapq
from typing import List


def solve_brute(target, startFuel, stations):
    return solve_optimal(target, startFuel, stations)


def solve_optimal(target, startFuel, stations):
    heap = []
    fuel = startFuel
    stops = 0
    stations.append((target, 0))
    for loc, cap in stations:
        while fuel < loc:
            if not heap:
                return -1
            fuel -= heapq.heappop(heap)
            stops += 1
        heapq.heappush(heap, -cap)
    return stops


@pytest.mark.parametrize(
    "t,f,s,ex",
    [
        (1, 1, [], 0),
        (100, 1, [[10, 100]], -1),
        (100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2),
    ],
)
def test_opt(t, f, s, ex):
    assert solve_optimal(t, f, s[:]) == ex

"""
Problem: Maximum Units on a Truck
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Load truck with max units. Choose up to truckSize boxes.
Complexity: Time O(N log N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(boxTypes, truckSize):
    return solve_optimal(boxTypes, truckSize)


def solve_optimal(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: -x[1])
    total = 0
    for count, units in boxTypes:
        take = min(count, truckSize)
        total += take * units
        truckSize -= take
        if truckSize == 0:
            break
    return total


@pytest.mark.parametrize(
    "bt,ts,ex",
    [([[1, 3], [2, 2], [3, 1]], 4, 8), ([[5, 10], [2, 5], [4, 7], [3, 9]], 10, 91)],
)
def test_opt(bt, ts, ex):
    assert solve_optimal(bt, ts) == ex

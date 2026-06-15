"""
Problem: Maximum Units on a Truck
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Load truck with max units. Choose up to truckSize boxes.
Complexity: Time O(N log N), Space O(1)
"""

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


if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [2, 2], [3, 1]], 4, 8),
        ([[5, 10], [2, 5], [4, 7], [3, 9]], 10, 91),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for bt, ts, ex in test_cases:
        assert solve_optimal(bt, ts) == ex
    print("All tests passed successfully!")

"""
Problem: Peak Index in a Mountain Array
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Find peak index in mountain array.
Complexity: Time O(log N), Space O(1)
"""

from typing import List


def solve_brute(arr):
    return arr.index(max(arr))


def solve_optimal(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] > arr[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return l


if __name__ == "__main__":
    test_cases = [([0, 1, 0], 1), ([0, 2, 1, 0], 1), ([0, 10, 5, 2], 1)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arr, ex in test_cases:
        assert solve_optimal(arr) == ex
    print("All tests passed successfully!")

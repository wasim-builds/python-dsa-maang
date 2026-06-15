"""
Problem: Minimum Absolute Difference
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Find all pairs with minimum absolute difference. Return sorted.
Complexity: Time O(N log N), Space O(N)
"""

from typing import List


def solve_brute(arr):
    return solve_optimal(arr)


def solve_optimal(arr):
    arr.sort()
    mn = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))
    return [
        [arr[i], arr[i + 1]] for i in range(len(arr) - 1) if arr[i + 1] - arr[i] == mn
    ]


if __name__ == "__main__":
    test_cases = [
        ([4, 2, 1, 3], [[1, 2], [2, 3], [3, 4]]),
        ([1, 3, 6, 10, 15], [[1, 3]]),
    ]
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

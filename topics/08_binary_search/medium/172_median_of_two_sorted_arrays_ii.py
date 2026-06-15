"""
Problem: Find K Closest Elements
Difficulty: Medium  Companies: LinkedIn,Google,Facebook,Amazon
Problem Statement: Given sorted array, find k closest elements to x. Return sorted.
Complexity: Time O(log N), Space O(1)
"""

from typing import List


def solve_brute(arr, k, x):
    arr.sort(key=lambda n: abs(n - x))
    return sorted(arr[:k])


def solve_optimal(arr, k, x):
    l, r = 0, len(arr) - k
    while l < r:
        mid = (l + r) // 2
        if x - arr[mid] > arr[mid + k] - x:
            l = mid + 1
        else:
            r = mid
    return arr[l : l + k]


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arr, k, x, ex in test_cases:
        assert solve_optimal(arr, k, x) == ex
    print("All tests passed successfully!")

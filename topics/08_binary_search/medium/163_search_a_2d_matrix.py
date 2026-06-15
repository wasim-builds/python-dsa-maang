"""
Problem: Search a 2D Matrix
Difficulty: Medium
Topic: 08_binary_search
Companies: Amazon, Microsoft, Meta, Bloomberg, Apple

Problem Statement:
You are given an `m x n` integer matrix `matrix` with the following two properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.
Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.
You must write a solution in `O(log(m * n))` time complexity.

Complexity Proof:
- Time Complexity: O(log(M * N)) where M is rows and N is cols. We conceptually flatten the 2D matrix into a 1D array of length M*N and perform a standard binary search.
- Space Complexity: O(1) because we only use two pointers (`l`, `r`) for the binary search.
"""

from typing import List


# OPTIMAL (Double Binary Search / Flattened Binary Search)
# Time: O(log(M * N)), Space: O(1)
def solve_optimal(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    ROWS, COLS = len(matrix), len(matrix[0])

    # Optional Phase 1: Binary search for the correct row (O(log M))
    # Optional Phase 2: Binary search within the row (O(log N))
    # OR, conceptually treat it as a 1D array:

    l, r = 0, ROWS * COLS - 1

    while l <= r:
        mid = (l + r) // 2
        # Map 1D mid index to 2D row and col
        row = mid // COLS
        col = mid % COLS

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            l = mid + 1
        else:
            r = mid - 1

    return False


# BRUTE FORCE
# Time: O(M * N), Space: O(1)
def solve_brute(matrix: List[List[int]], target: int) -> bool:
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == target:
                return True
    return False


if __name__ == "__main__":
    test_cases = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ([[1]], 1, True),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for matrix, target, expected in test_cases:
        assert solve_brute(matrix, target) == expected
    print("All tests passed successfully!")

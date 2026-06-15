"""
Problem: Container With Most Water
Difficulty: Medium
Topic: 09_two_pointers_sliding_window
Companies: Amazon, Google, Microsoft, Meta, Apple

Problem Statement:
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Complexity Proof:
- Time Complexity: O(N) because the two pointers (`l` and `r`) traverse the array exactly once from opposite ends.
- Space Complexity: O(1) because we only store a few variables (`l`, `r`, `max_area`).
"""

from typing import List


# BRUTE FORCE
# Time: O(N^2), Space: O(1)
def solve_brute(height: List[int]) -> int:
    max_area = 0
    for l in range(len(height)):
        for r in range(l + 1, len(height)):
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)
    return max_area


# OPTIMAL
# Time: O(N), Space: O(1)
def solve_optimal(height: List[int]) -> int:
    max_area = 0
    l = 0
    r = len(height) - 1

    while l < r:
        area = min(height[l], height[r]) * (r - l)
        max_area = max(max_area, area)

        # Move the pointer pointing to the shorter line
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area


if __name__ == "__main__":
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for height, expected in test_cases:
        assert solve_brute(height) == expected
    print("All tests passed successfully!")

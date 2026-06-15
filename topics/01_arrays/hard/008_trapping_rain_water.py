"""
Problem: Trapping Rain Water
Difficulty: Hard
Topic: 01_arrays
Companies: Google, Amazon, Facebook, Microsoft, Apple

Problem Statement:
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Complexity Proof:
- Time Complexity: O(N) since we use two pointers to scan the array exactly once.
- Space Complexity: O(1) since we only maintain a few integer variables (`l`, `r`, `leftMax`, `rightMax`, `res`).
"""

from typing import List


# BRUTE FORCE
# Time: O(N^2), Space: O(1)
def solve_brute(height: List[int]) -> int:
    res = 0
    for i in range(len(height)):
        leftMax = rightMax = height[i]
        for j in range(i):
            leftMax = max(leftMax, height[j])
        for j in range(i + 1, len(height)):
            rightMax = max(rightMax, height[j])
        res += min(leftMax, rightMax) - height[i]
    return res


# OPTIMAL (Two Pointers)
# Time: O(N), Space: O(1)
def solve_optimal(height: List[int]) -> int:
    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]

    return res


if __name__ == "__main__":
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([], 0),
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

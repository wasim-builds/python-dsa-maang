"""
Problem: Largest Rectangle in Histogram
Difficulty: Hard
Topic: 04_stacks_queues
Companies: Amazon, Google, Microsoft, Meta, Apple

Problem Statement:
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

Complexity Proof:
- Time Complexity: O(N) where N is the number of bars. We push and pop each index from the stack at most once.
- Space Complexity: O(N) for the monotonic stack which stores the indices.
"""

from typing import List


# OPTIMAL (Monotonic Increasing Stack)
# Time: O(N), Space: O(N)
def solve_optimal(heights: List[int]) -> int:
    maxArea = 0
    stack = []  # pair: (index, height)

    for i, h in enumerate(heights):
        start = i
        # While current height is less than the top of the stack, pop and calculate area
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index  # extend the starting point of the current height backwards
        stack.append((start, h))

    # Calculate areas for the remaining elements in the stack
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))

    return maxArea


# BRUTE FORCE
# Time: O(N^2), Space: O(1)
def solve_brute(heights: List[int]) -> int:
    maxArea = 0
    for i in range(len(heights)):
        minHeight = heights[i]
        for j in range(i, len(heights)):
            minHeight = min(minHeight, heights[j])
            maxArea = max(maxArea, minHeight * (j - i + 1))
    return maxArea


if __name__ == "__main__":
    test_cases = [([2, 1, 5, 6, 2, 3], 10), ([2, 4], 4), ([1, 1], 2)]

    for heights, expected in test_cases:
        assert solve_brute(heights) == expected
    print("All tests passed successfully!")

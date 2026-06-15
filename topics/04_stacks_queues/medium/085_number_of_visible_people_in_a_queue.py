"""
Problem: Number of Visible People in a Queue
Difficulty: Medium  Companies: Google,Amazon
Problem Statement: People stand in line. heights[i] is height of ith person. Return how many people each can see to right.
Complexity: Time O(N), Space O(N)
"""

import pytest
from typing import List


def solve_brute(heights):
    n = len(heights)
    res = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if all(heights[k] < heights[j] for k in range(i + 1, j)):
                if (
                    heights[j] > max(heights[i + 1 : j + 1] or [0])
                    or heights[j] >= heights[j]
                ):
                    pass
            if heights[j] > max(heights[i + 1 : j] or [0]):
                res[i] += 1
                if heights[j] >= heights[i]:
                    break
    return res


def solve_optimal(heights):
    n = len(heights)
    res = [0] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and heights[i] > stack[-1]:
            res[i] += 1
            stack.pop()
        if stack:
            res[i] += 1
        stack.append(heights[i])
    return res


@pytest.mark.parametrize(
    "h,ex",
    [([10, 6, 8, 5, 11, 9], [3, 1, 2, 1, 1, 0]), ([5, 1, 2, 3, 10], [4, 1, 1, 1, 0])],
)
def test_opt(h, ex):
    assert solve_optimal(h) == ex

"""
Problem: Number of Visible People in a Queue
Difficulty: Medium  Companies: Google,Amazon
Problem Statement: People stand in line. heights[i] is height of ith person. Return how many people each can see to right.
Complexity: Time O(N), Space O(N)
"""

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


if __name__ == "__main__":
    test_cases = [
        ([10, 6, 8, 5, 11, 9], [3, 1, 2, 1, 1, 0]),
        ([5, 1, 2, 3, 10], [4, 1, 1, 1, 0]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for h, ex in test_cases:
        assert solve_optimal(h) == ex
    print("All tests passed successfully!")

"""
Problem: Daily Temperatures
Difficulty: Medium
Topic: 04_stacks_queues
Companies: Amazon, Meta, Microsoft, Apple, Google

Problem Statement:
Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature.
If there is no future day for which this is possible, keep `answer[i] == 0` instead.

Complexity Proof:
- Time Complexity: O(N) where N is the number of temperatures. Each element is pushed and popped from the stack at most once.
- Space Complexity: O(N) for the monotonic stack storing the indices of the temperatures.
"""

from typing import List


# OPTIMAL (Monotonic Decreasing Stack)
# Time: O(N), Space: O(N)
def solve_optimal(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []  # pair: (temp, index)

    for i, t in enumerate(temperatures):
        # While stack is not empty and current temp is greater than stack top
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append((t, i))

    return res


# BRUTE FORCE
# Time: O(N^2), Space: O(1) (excluding output array)
def solve_brute(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    for i in range(len(temperatures)):
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                res[i] = j - i
                break
    return res


if __name__ == "__main__":
    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for temperatures, expected in test_cases:
        assert solve_brute(temperatures) == expected
    print("All tests passed successfully!")

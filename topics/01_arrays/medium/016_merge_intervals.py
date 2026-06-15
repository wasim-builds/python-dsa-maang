"""
Problem: Merge Intervals
Difficulty: Medium
Topic: 01_arrays
Companies: Google, Meta, Amazon, Microsoft, Bloomberg

Problem Statement:
Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Complexity Proof:
- Time Complexity: O(N log N) because we must sort the intervals by their start times first. The subsequent merge process takes O(N).
- Space Complexity: O(N) or O(log N) depending on the sorting algorithm. The output array can take O(N) space if no intervals overlap.
"""

from typing import List


# BRUTE FORCE
# Time: O(N^2), Space: O(N)
def solve_brute(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    # We still need to sort, but let's simulate a less efficient approach
    intervals.sort(key=lambda i: i[0])
    res = [intervals[0]]

    for i in range(1, len(intervals)):
        last_added = res[-1]
        if last_added[1] >= intervals[i][0]:
            res[-1][1] = max(last_added[1], intervals[i][1])
        else:
            res.append(intervals[i])

    return res


# OPTIMAL
# Time: O(N log N), Space: O(N) or O(1) extra space
def solve_optimal(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda i: i[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = output[-1][1]

        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])

    return output


if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for input_data, expected in test_cases:
        assert solve_brute(input_data) == expected
    print("All tests passed successfully!")

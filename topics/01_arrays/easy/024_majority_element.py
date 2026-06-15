"""
Problem: Majority Element
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon,Apple

Problem Statement:
Find the element appearing more than n/2 times. Use O(1) space (Boyer-Moore).

Complexity Proof:
- Time: O(N)
- Space: O(1)
"""

from typing import List


def solve_brute(nums):
    from collections import Counter

    return max(Counter(nums), key=Counter(nums).get)


def solve_optimal(nums):
    count = 0
    cand = None
    for n in nums:
        if count == 0:
            cand = n
        count += 1 if n == cand else -1
    return cand


if __name__ == "__main__":
    test_cases = [([3, 2, 3], 3), ([2, 2, 1, 1, 1, 2, 2], 2)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, expected in test_cases:
        assert solve_optimal(nums) == expected
    print("All tests passed successfully!")

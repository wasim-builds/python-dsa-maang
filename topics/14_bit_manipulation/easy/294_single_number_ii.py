"""
Problem: Single Number II
Difficulty: Easy  Companies: Amazon,Google,Bloomberg
Problem Statement: Find element appearing once; all others appear three times. O(1) space.
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(nums):
    from collections import Counter

    return [k for k, v in Counter(nums).items() if v == 1][0]


def solve_optimal(nums):
    ones = twos = 0
    for n in nums:
        ones = (ones ^ n) & ~twos
        twos = (twos ^ n) & ~ones
    return ones


if __name__ == "__main__":
    test_cases = [([2, 2, 3, 2], 3), ([0, 1, 0, 1, 0, 1, 99], 99)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, ex in test_cases:
        assert solve_optimal(nums) == ex
    print("All tests passed successfully!")

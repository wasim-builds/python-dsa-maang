"""
Problem: Single Number III
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Find two elements appearing once; all others appear twice.
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(nums):
    from collections import Counter

    return [k for k, v in Counter(nums).items() if v == 1]


def solve_optimal(nums):
    xor = 0
    for n in nums:
        xor ^= n
    diff = xor & (-xor)
    a = b = 0
    for n in nums:
        if n & diff:
            a ^= n
        else:
            b ^= n
    return [a, b]


if __name__ == "__main__":
    test_cases = [([1, 2, 1, 3, 2, 5], {3, 5}), ([1, 2], {1, 2})]

    for nums, ex in test_cases:
        assert set(solve_optimal(nums)) == ex
    print("All tests passed successfully!")

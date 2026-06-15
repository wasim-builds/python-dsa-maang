"""
Problem: Total Hamming Distance
Difficulty: Medium  Companies: Amazon,Google
Problem Statement: Sum of Hamming distances between all pairs of integers.
Complexity: Time O(N * 32), Space O(1)
"""

from typing import List


def solve_brute(nums):
    def hd(a, b):
        count = 0
        while a or b:
            count += (a ^ b) & 1
            a >>= 1
            b >>= 1
        return count

    return sum(
        hd(nums[i], nums[j]) for i in range(len(nums)) for j in range(i + 1, len(nums))
    )


def solve_optimal(nums):
    total = 0
    n = len(nums)
    for bit in range(32):
        ones = sum(1 for x in nums if (x >> bit) & 1)
        total += ones * (n - ones)
    return total


if __name__ == "__main__":
    test_cases = [([4, 14, 2], 6), ([4, 14, 4], 4)]
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

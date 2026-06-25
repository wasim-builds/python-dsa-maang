"""
Problem: Sum of All Subset XOR Totals
Difficulty: Medium  Companies: Amazon,Google
Problem Statement: Return sum of XOR totals for all subsets of nums.
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(nums):
    from itertools import combinations

    total = 0
    for r in range(len(nums) + 1):
        for combo in combinations(nums, r):
            xor = 0
            for n in combo:
                xor ^= n
            total += xor
    return total


def solve_optimal(nums):
    or_total = 0
    for n in nums:
        or_total |= n
    return or_total * (1 << (len(nums) - 1))


if __name__ == "__main__":
    test_cases = [([1, 3], 6)]

    for nums, ex in test_cases:
        assert solve_brute(nums) == ex
    print("All tests passed successfully!")

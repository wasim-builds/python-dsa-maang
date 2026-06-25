"""
Problem: Largest Number
Difficulty: Hard  Companies: Amazon,Google,Bloomberg
Problem Statement: Arrange numbers to form the largest number.
Complexity: Time O(N log N), Space O(N)
"""

from typing import List
from functools import cmp_to_key


def solve_brute(nums):
    return solve_optimal(nums)


def solve_optimal(nums):
    def cmp(a, b):
        return (int(a + b) > int(b + a)) - (int(a + b) < int(b + a))

    nums = sorted(map(str, nums), key=cmp_to_key(cmp), reverse=True)
    return "".join(nums).lstrip("0") or "0"


if __name__ == "__main__":
    test_cases = [([10, 2], "210"), ([3, 30, 34, 5, 9], "9534330"), ([0, 0], "0")]

    for nums, ex in test_cases:
        assert solve_optimal(nums) == ex
    print("All tests passed successfully!")

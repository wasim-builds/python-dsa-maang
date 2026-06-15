"""
Problem: Partition Equal Subset Sum
Difficulty: Medium  Companies: Amazon,Google,Meta,Microsoft
Problem Statement: Partition array into two subsets with equal sum.
Complexity: Time O(N * sum/2), Space O(sum/2)
"""

from typing import List


def solve_brute(nums):
    target = sum(nums)
    if target % 2:
        return False
    target //= 2
    dp = {0}
    for n in nums:
        dp |= {s + n for s in dp}
    return target in dp


def solve_optimal(nums):
    return solve_brute(nums)


if __name__ == "__main__":
    test_cases = [([1, 5, 11, 5], True), ([1, 2, 3, 5], False)]
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

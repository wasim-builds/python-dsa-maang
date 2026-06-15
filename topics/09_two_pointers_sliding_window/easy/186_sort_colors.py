"""
Problem: Sort Colors
Difficulty: Easy  Companies: Microsoft,Amazon,Meta,Google
Problem Statement: Sort array with values 0,1,2 in-place using one pass (Dutch Flag).
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(nums):
    nums.sort()


def solve_optimal(nums):
    l = mid = 0
    r = len(nums) - 1
    while mid <= r:
        if nums[mid] == 0:
            nums[l], nums[mid] = nums[mid], nums[l]
            l += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[r] = nums[r], nums[mid]
            r -= 1
        else:
            mid += 1


if __name__ == "__main__":
    test_cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, ex in test_cases:
        solve_optimal(nums)
        assert nums == ex
    print("All tests passed successfully!")

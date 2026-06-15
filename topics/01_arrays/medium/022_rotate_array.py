"""
Problem: Rotate Array
Difficulty: Medium
Topic: 01_arrays  Companies: Microsoft,Amazon,Apple
Problem Statement: Rotate array to right by k steps in-place.
Complexity: Time O(N), Space O(1) reverse approach
"""

from typing import List


def solve_brute(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]


def solve_optimal(nums, k):
    k %= len(nums)

    def rev(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    rev(0, len(nums) - 1)
    rev(0, k - 1)
    rev(k, len(nums) - 1)


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, k, ex in test_cases:
        solve_optimal(nums, k)
        assert nums == ex
    print("All tests passed successfully!")

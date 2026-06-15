"""
Problem: Squares of a Sorted Array
Difficulty: Easy  Companies: Google,Amazon,Microsoft
Problem Statement: Return sorted array of squares of sorted array.
Complexity: Time O(N), Space O(N)
"""

from typing import List


def solve_brute(nums):
    return sorted(x * x for x in nums)


def solve_optimal(nums):
    n = len(nums)
    res = [0] * n
    l, r = 0, n - 1
    pos = n - 1
    while l <= r:
        if abs(nums[l]) >= abs(nums[r]):
            res[pos] = nums[l] * nums[l]
            l += 1
        else:
            res[pos] = nums[r] * nums[r]
            r -= 1
        pos -= 1
    return res


if __name__ == "__main__":
    test_cases = [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
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
        assert solve_optimal(nums) == ex
    print("All tests passed successfully!")

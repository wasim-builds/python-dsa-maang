"""
Problem: Smallest Subarrays With Maximum Bitwise OR
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: For each index i, find smallest j>=i where OR of nums[i..j] equals OR of nums[i..n-1].
Complexity: Time O(N * 32), Space O(N)
"""

from typing import List


def solve_brute(nums):
    return solve_optimal(nums)


def solve_optimal(nums):
    n = len(nums)
    res = [0] * n
    last = [0] * 32
    for i in range(n - 1, -1, -1):
        for b in range(32):
            if (nums[i] >> b) & 1:
                last[b] = i
        res[i] = max(1, max(last) - i + 1)
    return res


if __name__ == "__main__":
    test_cases = [([1, 0, 2, 1, 3], [3, 3, 2, 2, 1]), ([1, 2], [2, 1])]
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

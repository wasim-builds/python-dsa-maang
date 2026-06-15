"""
Problem: Permutations II
Difficulty: Hard  Companies: Amazon,LinkedIn,Microsoft
Problem Statement: Given collection with duplicates, return all unique permutations.
Complexity: Time O(N! * N), Space O(N)
"""

from typing import List


def solve_brute(nums):
    return solve_optimal(nums)


def solve_optimal(nums):
    nums.sort()
    res = []
    used = [False] * len(nums)

    def bt(perm):
        if len(perm) == len(nums):
            res.append(perm[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            perm.append(nums[i])
            bt(perm)
            perm.pop()
            used[i] = False

    bt([])
    return res


if __name__ == "__main__":
    test_cases = [
        ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
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
        assert sorted(solve_optimal(nums)) == sorted(ex)
    print("All tests passed successfully!")

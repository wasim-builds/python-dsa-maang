"""
Problem: Subarrays with K Different Integers
Difficulty: Hard  Companies: Google,Amazon,Facebook
Problem Statement: Return number of subarrays with exactly k different integers.
Complexity: Time O(N), Space O(N)
"""

from typing import List


def at_most_k(nums, k):
    count = {}
    l = res = 0
    for r in range(len(nums)):
        count[nums[r]] = count.get(nums[r], 0) + 1
        while len(count) > k:
            count[nums[l]] -= 1
            if count[nums[l]] == 0:
                del count[nums[l]]
            l += 1
        res += r - l + 1
    return res


def solve_brute(nums, k):
    count = {}
    l = cnt = 0
    for r in range(len(nums)):
        count[nums[r]] = count.get(nums[r], 0) + 1
        while len(count) > k:
            count[nums[l]] -= 1
            (count.pop(nums[l]) if count[nums[l]] == 0 else None)
            l += 1
    return at_most_k(nums, k) - at_most_k(nums, k - 1)


def solve_optimal(nums, k):
    return at_most_k(nums, k) - at_most_k(nums, k - 1)


if __name__ == "__main__":
    test_cases = [([1, 2, 1, 2, 3], 2, 7), ([1, 2, 1, 3, 4], 3, 3)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, k, ex in test_cases:
        assert solve_optimal(nums, k) == ex
    print("All tests passed successfully!")

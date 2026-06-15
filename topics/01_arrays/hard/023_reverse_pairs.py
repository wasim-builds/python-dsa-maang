"""
Problem: Reverse Pairs
Difficulty: Hard
Topic: 01_arrays  Companies: Google,Microsoft,Amazon
Problem Statement: Return count of reverse pairs i<j where nums[i]>2*nums[j].
Complexity: Time O(N log N) merge sort, Space O(N)
"""

from typing import List


def solve_brute(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > 2 * nums[j]:
                count += 1
    return count


def solve_optimal(nums):
    def merge_count(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        L, lc = merge_count(arr[:mid])
        R, rc = merge_count(arr[mid:])
        count = lc + rc
        j = 0
        for a in L:
            while j < len(R) and a > 2 * R[j]:
                j += 1
            count += j
        merged = sorted(L + R)
        return merged, count

    _, ans = merge_count(nums)
    return ans


if __name__ == "__main__":
    test_cases = [([1, 3, 2, 3, 1], 2)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, ex in test_cases:
        assert solve_brute(nums) == ex
    print("All tests passed successfully!")

"""
Problem: Count of Smaller Numbers After Self
Difficulty: Hard  Companies: Google,Facebook,Amazon
Problem Statement: Return counts array where counts[i] is how many smaller elements appear after nums[i].
Complexity: Time O(N log N) merge sort, Space O(N)
"""

import pytest
from typing import List


def solve_brute(nums):
    n = len(nums)
    counts = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                counts[i] += 1
    return counts


def solve_optimal(nums):
    result = [0] * len(nums)
    indexed = list(enumerate(nums))

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        merged = []
        j = 0
        for i in range(len(left)):
            while j < len(right) and right[j][1] < left[i][1]:
                merged.append(right[j])
                j += 1
            result[left[i][0]] += j
            merged.append(left[i])
        return merged + right[j:]

    merge_sort(indexed)
    return result


@pytest.mark.parametrize(
    "nums,ex", [([5, 2, 6, 1], [2, 1, 1, 0]), ([1], [0]), ([-1], [0])]
)
def test_opt(nums, ex):
    assert solve_optimal(nums) == ex


@pytest.mark.parametrize("nums,ex", [([5, 2, 6, 1], [2, 1, 1, 0])])
def test_brute(nums, ex):
    assert solve_brute(nums) == ex

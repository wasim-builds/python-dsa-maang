"""
Problem: Count of Smaller Numbers After Self
Difficulty: Hard  Companies: Google,Facebook,Amazon
Problem Statement: Return counts array where counts[i] is how many smaller elements appear after nums[i].
Complexity: Time O(N log N) merge sort, Space O(N)
"""

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


if __name__ == "__main__":
    test_cases = [([5, 2, 6, 1], [2, 1, 1, 0])]
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

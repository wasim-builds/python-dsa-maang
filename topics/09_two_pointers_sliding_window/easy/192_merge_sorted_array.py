"""
Problem: Merge Sorted Array
Difficulty: Easy  Companies: Amazon,Microsoft,Google,Meta
Problem Statement: Merge nums2 into nums1 in sorted order. nums1 has space for m+n elements.
Complexity: Time O(M+N), Space O(1)
"""

from typing import List


def solve_brute(nums1, m, nums2, n):
    nums1[m : m + n] = nums2
    nums1.sort()


def solve_optimal(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for n1, m, n2, n, ex in test_cases:
        solve_optimal(n1, m, n2, n)
        assert n1 == ex
    print("All tests passed successfully!")

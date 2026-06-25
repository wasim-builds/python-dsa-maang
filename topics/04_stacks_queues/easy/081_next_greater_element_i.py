"""
Problem: Next Greater Element I
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: For each element in nums1 (subset of nums2), find next greater element in nums2.
Complexity: Time O(N), Space O(N)
"""

from typing import List


def solve_brute(nums1, nums2):
    res = []
    for n in nums1:
        found = False
        nge = -1
        for m in nums2:
            if found and m > n:
                nge = m
                break
            if m == n:
                found = True
        res.append(nge)
    return res


def solve_optimal(nums1, nums2):
    nge = {}
    stack = []
    for n in nums2:
        while stack and stack[-1] < n:
            nge[stack.pop()] = n
        stack.append(n)
    return [nge.get(n, -1) for n in nums1]


if __name__ == "__main__":
    test_cases = [
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
    ]

    for n1, n2, ex in test_cases:
        assert solve_optimal(n1, n2) == ex
    print("All tests passed successfully!")

"""
Problem: Median of Two Sorted Arrays
Difficulty: Hard
Topic: 01_arrays  Companies: Amazon,Google,Microsoft,Meta,Apple
Problem Statement: Given two sorted arrays nums1 and nums2, return the median of the two sorted arrays in O(log(m+n)) time.
Complexity: Time O(log(min(m,n))), Space O(1)
"""

import pytest
from typing import List


def solve_brute(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    return merged[n // 2] if n % 2 == 1 else (merged[n // 2 - 1] + merged[n // 2]) / 2.0


def solve_optimal(nums1, nums2):
    A, B = nums1, nums2
    if len(A) > len(B):
        A, B = B, A
    total = len(A) + len(B)
    half = total // 2
    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2
        j = half - i - 2
        Aleft = A[i] if i >= 0 else float("-inf")
        Aright = A[i + 1] if i + 1 < len(A) else float("inf")
        Bleft = B[j] if j >= 0 else float("-inf")
        Bright = B[j + 1] if j + 1 < len(B) else float("inf")
        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1


@pytest.mark.parametrize(
    "n1,n2,ex", [([1, 3], [2], 2.0), ([1, 2], [3, 4], 2.5), ([0, 0], [0, 0], 0.0)]
)
def test_opt(n1, n2, ex):
    assert solve_optimal(n1, n2) == ex


@pytest.mark.parametrize("n1,n2,ex", [([1, 3], [2], 2.0)])
def test_brute(n1, n2, ex):
    assert solve_brute(n1, n2) == ex

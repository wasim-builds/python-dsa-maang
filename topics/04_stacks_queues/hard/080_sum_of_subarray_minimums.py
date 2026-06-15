"""
Problem: Sum of Subarray Minimums
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Return sum of min values of all subarrays. Answer modulo 1e9+7.
Complexity: Time O(N), Space O(N)
"""

import pytest
from typing import List

MOD = 10**9 + 7


def solve_brute(arr):
    res = 0
    for i in range(len(arr)):
        m = arr[i]
        for j in range(i, len(arr)):
            m = min(m, arr[j])
            res += m
    return res % MOD


def solve_optimal(arr):
    n = len(arr)
    stack = []
    res = 0
    for i in range(n + 1):
        while stack and (i == n or arr[stack[-1]] >= arr[i]):
            mid = stack.pop()
            l = stack[-1] if stack else -1
            res += (mid - l) * (i - mid) * arr[mid]
        stack.append(i)
    return res % MOD


@pytest.mark.parametrize("arr,ex", [([3, 1, 2, 4], 17), ([11, 81, 94, 43, 3], 444)])
def test_opt(arr, ex):
    assert solve_optimal(arr) == ex


@pytest.mark.parametrize("arr,ex", [([3, 1, 2, 4], 17)])
def test_brute(arr, ex):
    assert solve_brute(arr) == ex

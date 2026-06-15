"""
Problem: Count Triplets That Can Form Two Arrays of Equal XOR
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Count triplets (i,j,k) where XOR(i..j-1)==XOR(j..k).
Complexity: Time O(N^2), Space O(N)
"""

import pytest
from typing import List


def solve_brute(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j, n):
                a = b = 0
                for x in range(i, j):
                    a ^= arr[x]
                for x in range(j, k + 1):
                    b ^= arr[x]
                if a == b:
                    count += 1
    return count


def solve_optimal(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        xor = arr[i]
        for k in range(i + 1, n):
            xor ^= arr[k]
            if xor == 0:
                count += k - i
    return count


@pytest.mark.parametrize("arr,ex", [([2, 3, 1, 6, 7], 4), ([1, 1, 1, 1, 1], 10)])
def test_opt(arr, ex):
    assert solve_optimal(arr) == ex

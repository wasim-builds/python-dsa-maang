"""
Problem: Bitwise ORs of Subarrays
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Count distinct bitwise ORs of all subarrays.
Complexity: Time O(N * 32), Space O(N * 32)
"""

import pytest
from typing import List


def solve_brute(arr):
    res = set()
    for i in range(len(arr)):
        xor = 0
        for j in range(i, len(arr)):
            xor |= arr[j]
            res.add(xor)
    return len(res)


def solve_optimal(arr):
    res = set()
    cur = set()
    for n in arr:
        cur = {x | n for x in cur} | {n}
        res |= cur
    return len(res)


@pytest.mark.parametrize("arr,ex", [([0], 1), ([1, 1, 2], 3), ([1, 2, 4], 6)])
def test_opt(arr, ex):
    assert solve_optimal(arr) == ex

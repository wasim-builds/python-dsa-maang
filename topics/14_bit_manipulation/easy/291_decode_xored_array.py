"""
Problem: Decode XORed Array
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Given encoded and first element, recover original array.
Complexity: Time O(N), Space O(N)
"""

import pytest
from typing import List


def solve_brute(encoded, first):
    return solve_optimal(encoded, first)


def solve_optimal(encoded, first):
    arr = [first]
    for e in encoded:
        arr.append(arr[-1] ^ e)
    return arr


@pytest.mark.parametrize(
    "enc,f,ex", [([1, 2, 3], 1, [1, 0, 2, 1]), ([6, 2, 7, 3], 4, [4, 2, 0, 7, 4])]
)
def test_opt(enc, f, ex):
    assert solve_optimal(enc, f) == ex

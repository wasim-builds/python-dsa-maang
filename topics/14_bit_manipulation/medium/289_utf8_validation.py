"""
Problem: UTF-8 Validation
Difficulty: Medium  Companies: Facebook,Google,Amazon
Problem Statement: Given array of integers (bytes), validate if it is valid UTF-8 encoding.
Complexity: Time O(N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(data):
    return solve_optimal(data)


def solve_optimal(data):
    i = 0
    while i < len(data):
        b = data[i]
        if b >> 7 == 0:
            n = 0
        elif b >> 5 == 0b110:
            n = 1
        elif b >> 4 == 0b1110:
            n = 2
        elif b >> 3 == 0b11110:
            n = 3
        else:
            return False
        i += 1
        for _ in range(n):
            if i >= len(data) or data[i] >> 6 != 0b10:
                return False
            i += 1
    return True


@pytest.mark.parametrize("d,ex", [([197, 130, 1], True), ([235, 140, 4], False)])
def test_opt(d, ex):
    assert solve_optimal(d) == ex

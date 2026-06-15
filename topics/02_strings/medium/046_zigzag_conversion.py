"""
Problem: Zigzag Conversion
Difficulty: Medium
Topic: 02_strings  Companies: Amazon,Bloomberg,Microsoft
Problem Statement: Write string in zigzag pattern on given numRows and return reading row by row.
Complexity: Time O(N), Space O(N)
"""

import pytest


def solve_brute(s, numRows):
    return solve_optimal(s, numRows)


def solve_optimal(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [""] * (numRows)
    cur = 0
    go_down = False
    for c in s:
        rows[cur] += c
        if cur == 0 or cur == numRows - 1:
            go_down = not go_down
        cur += 1 if go_down else -1
    return "".join(rows)


@pytest.mark.parametrize(
    "s,r,ex",
    [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
    ],
)
def test_opt(s, r, ex):
    assert solve_optimal(s, r) == ex

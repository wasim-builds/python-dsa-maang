"""
Problem: N-Queens
Difficulty: Hard  Companies: Amazon,Google,Microsoft
Problem Statement: Return all distinct solutions to N-queens puzzle as board configurations.
Complexity: Time O(N!), Space O(N^2)
"""

import pytest
from typing import List


def solve_brute(n):
    return solve_optimal(n)


def solve_optimal(n):
    res = []
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [["."] * n for _ in range(n)]

    def bt(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or r + c in pos_diag or r - c in neg_diag:
                continue
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"
            bt(r + 1)
            cols.discard(c)
            pos_diag.discard(r + c)
            neg_diag.discard(r - c)
            board[r][c] = "."

    bt(0)
    return res


@pytest.mark.parametrize("n,ex_len", [(4, 2), (1, 1), (8, 92)])
def test_opt(n, ex_len):
    assert len(solve_optimal(n)) == ex_len

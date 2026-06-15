"""
Problem: N-Queens
Difficulty: Hard  Companies: Amazon,Google,Microsoft
Problem Statement: Return all distinct solutions to N-queens puzzle as board configurations.
Complexity: Time O(N!), Space O(N^2)
"""

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


if __name__ == "__main__":
    test_cases = [(4, 2), (1, 1), (8, 92)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for n, ex_len in test_cases:
        assert len(solve_optimal(n)) == ex_len
    print("All tests passed successfully!")

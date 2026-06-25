"""
Problem: N-Queens II
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Return number of distinct solutions to N-queens puzzle.
Complexity: Time O(N!), Space O(N)
"""


def solve_brute(n):
    return solve_optimal(n)


def solve_optimal(n):
    count = [0]
    cols = set()
    pos_diag = set()
    neg_diag = set()

    def bt(r):
        if r == n:
            count[0] += 1
            return
        for c in range(n):
            if c in cols or r + c in pos_diag or r - c in neg_diag:
                continue
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            bt(r + 1)
            cols.discard(c)
            pos_diag.discard(r + c)
            neg_diag.discard(r - c)

    bt(0)
    return count[0]


if __name__ == "__main__":
    test_cases = [(4, 2), (1, 1), (8, 92)]

    for n, ex in test_cases:
        assert solve_optimal(n) == ex
    print("All tests passed successfully!")

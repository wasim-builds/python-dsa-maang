"""
Problem: Generate Parentheses
Difficulty: Easy  Companies: Amazon,Google,Meta,Bloomberg,Microsoft
Problem Statement: Generate all combinations of n pairs of well-formed parentheses.
Complexity: Time O(4^N / sqrt(N)) Catalan, Space O(N)
"""

from typing import List


def solve_brute(n):
    return solve_optimal(n)


def solve_optimal(n):
    res = []

    def bt(s, open, close):
        if len(s) == 2 * n:
            res.append(s)
            return
        if open < n:
            bt(s + "(", open + 1, close)
        if close < open:
            bt(s + ")", open, close + 1)

    bt("", 0, 0)
    return res


if __name__ == "__main__":
    test_cases = [(3, ["((()))", "(()())", "(())()", "()(())", "()()()"]), (1, ["()"])]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for n, ex in test_cases:
        assert sorted(solve_optimal(n)) == sorted(ex)
    print("All tests passed successfully!")

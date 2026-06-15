"""
Problem: Combination Sum III
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Find all combinations of k numbers that sum to n. Use 1-9 only once each.
Complexity: Time O(C(9,k)), Space O(k)
"""

import pytest
from typing import List


def solve_brute(k, n):
    return solve_optimal(k, n)


def solve_optimal(k, n):
    res = []

    def bt(start, comb, remaining):
        if len(comb) == k and remaining == 0:
            res.append(comb[:])
            return
        for i in range(start, 10):
            comb.append(i)
            bt(i + 1, comb, remaining - i)
            comb.pop()

    bt(1, [], n)
    return res


@pytest.mark.parametrize(
    "k,n,ex", [(3, 7, [[1, 2, 4]]), (3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]])]
)
def test_opt(k, n, ex):
    assert sorted(solve_optimal(k, n)) == sorted(ex)

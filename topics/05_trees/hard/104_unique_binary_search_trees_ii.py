"""
Problem: Unique Binary Search Trees II
Difficulty: Hard  Companies: Amazon,Google,Microsoft
Problem Statement: Return all structurally unique BSTs with values 1..n.
Complexity: Time O(4^N/N^1.5) Catalan, Space O(4^N/N^1.5)
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode
from typing import List, Optional
from functools import lru_cache


def solve_optimal(n):
    @lru_cache(None)
    def build(l, r):
        if l > r:
            return [None]
        res = []
        for v in range(l, r + 1):
            for left in build(l, v - 1):
                for right in build(v + 1, r):
                    root = TreeNode(v, left, right)
                    res.append(root)
        return res

    return build(1, n)


def solve_brute(n):
    return solve_optimal(n)


@pytest.mark.parametrize("n,ex_len", [(3, 5), (1, 1)])
def test_opt(n, ex_len):
    assert len(solve_optimal(n)) == ex_len

"""
Problem: Binary Tree Right Side View
Difficulty: Medium  Companies: Amazon,Meta,ByteDance,Microsoft,Bloomberg
Problem Statement: Given root, return values of nodes visible from right side, top to bottom.
Complexity: Time O(N), Space O(N)
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree
from collections import deque
from typing import List, Optional


def solve_brute(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level[-1])
    return res


def solve_optimal(root):
    return solve_brute(root)


@pytest.mark.parametrize(
    "arr,ex",
    [([1, 2, 3, None, 5, None, 4], [1, 3, 4]), ([1, None, 3], [1, 3]), ([], [])],
)
def test_opt(arr, ex):
    assert solve_optimal(list_to_tree(arr)) == ex

"""
Problem: Path Sum II
Difficulty: Medium  Companies: Amazon,Microsoft,Bloomberg
Problem Statement: Return all root-to-leaf paths summing to targetSum.
Complexity: Time O(N^2), Space O(N)
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree
from typing import List, Optional


def solve_brute(root, target):
    return solve_optimal(root, target)


def solve_optimal(root, target):
    res = []

    def dfs(node, path, remaining):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and remaining == node.val:
            res.append(path[:])
        dfs(node.left, path, remaining - node.val)
        dfs(node.right, path, remaining - node.val)
        path.pop()

    dfs(root, [], target)
    return res


@pytest.mark.parametrize(
    "arr,t,ex",
    [
        (
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
            22,
            [[5, 4, 11, 2], [5, 8, 4, 5]],
        )
    ],
)
def test_opt(arr, t, ex):
    assert sorted(solve_optimal(list_to_tree(arr), t)) == sorted(ex)

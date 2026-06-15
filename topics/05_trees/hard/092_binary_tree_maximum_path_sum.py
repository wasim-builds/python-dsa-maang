"""
Problem: Binary Tree Maximum Path Sum
Difficulty: Hard  Companies: Amazon,Facebook,Microsoft,Apple,Google
Problem Statement: A path is a sequence of nodes where each pair of adjacent nodes has edge. Return max path sum.
Complexity: Time O(N), Space O(H)
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree


def solve_optimal(root):
    res = [root.val]

    def dfs(node):
        if not node:
            return 0
        l = max(dfs(node.left), 0)
        r = max(dfs(node.right), 0)
        res[0] = max(res[0], node.val + l + r)
        return node.val + max(l, r)

    dfs(root)
    return res[0]


def solve_brute(root):
    return solve_optimal(root)


@pytest.mark.parametrize(
    "arr,ex", [([1, 2, 3], 6), ([-10, 9, 20, None, None, 15, 7], 42)]
)
def test_opt(arr, ex):
    assert solve_optimal(list_to_tree(arr)) == ex

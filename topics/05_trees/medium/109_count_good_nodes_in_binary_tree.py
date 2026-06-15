"""
Problem: Count Good Nodes in Binary Tree
Difficulty: Medium  Companies: Meta,DoorDash,Amazon,Microsoft
Problem Statement: Count nodes where no node in path from root has value greater.
Complexity: Time O(N), Space O(H)
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree


def solve_optimal(root):
    def dfs(node, maxVal):
        if not node:
            return 0
        res = 1 if node.val >= maxVal else 0
        maxVal = max(maxVal, node.val)
        return res + dfs(node.left, maxVal) + dfs(node.right, maxVal)

    return dfs(root, root.val)


def solve_brute(root):
    return solve_optimal(root)


@pytest.mark.parametrize(
    "arr,ex", [([3, 1, 4, 3, None, 1, 5], 4), ([3, 3, None, 4, 2], 3), ([1], 1)]
)
def test_opt(arr, ex):
    assert solve_optimal(list_to_tree(arr)) == ex

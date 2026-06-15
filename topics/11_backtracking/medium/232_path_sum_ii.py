"""
Problem: Path Sum II
Difficulty: Medium  Companies: Amazon,Microsoft,Bloomberg
Problem Statement: Return all root-to-leaf paths summing to targetSum.
Complexity: Time O(N^2), Space O(N)
"""

import sys, os

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


if __name__ == "__main__":
    test_cases = [
        (
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
            22,
            [[5, 4, 11, 2], [5, 8, 4, 5]],
        )
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arr, t, ex in test_cases:
        assert sorted(solve_optimal(list_to_tree(arr), t)) == sorted(ex)
    print("All tests passed successfully!")

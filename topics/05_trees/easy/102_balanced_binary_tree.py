"""
Problem: Balanced Binary Tree
Difficulty: Easy
Topic: 05_trees
Companies: Amazon, Microsoft, Meta, Google, Spotify

Problem Statement:
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Complexity Proof:
- Time Complexity: O(N) where N is the number of nodes in the tree. The optimal DFS approach computes heights bottom-up, visiting each node exactly once.
- Space Complexity: O(H) where H is the height of the tree. This accounts for the recursive call stack.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree
from typing import Optional


# BRUTE FORCE
# Time: O(N^2), Space: O(H)
# Calculating height explicitly at every node causes redundant traversals.
def solve_brute(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return solve_brute(root.left) and solve_brute(root.right)


# OPTIMAL (Recursive DFS returning (is_balanced, height))
# Time: O(N), Space: O(H)
def solve_optimal(root: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node:
            return [True, 0]

        left, right = dfs(node.left), dfs(node.right)

        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        height = 1 + max(left[1], right[1])

        return [balanced, height]

    return dfs(root)[0]


if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([], True),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arr, expected in test_cases:
        root = list_to_tree(arr)
        assert solve_brute(root) == expected
    print("All tests passed successfully!")

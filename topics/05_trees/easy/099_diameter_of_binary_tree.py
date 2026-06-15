"""
Problem: Diameter of Binary Tree
Difficulty: Easy
Topic: 05_trees
Companies: Meta, Amazon, Microsoft, Google, Apple

Problem Statement:
Given the `root` of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Complexity Proof:
- Time Complexity: O(N) where N is the number of nodes in the tree. We visit every node exactly once during the post-order DFS traversal.
- Space Complexity: O(H) where H is the height of the tree, representing the maximum depth of the recursive call stack.
"""

import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree
from typing import Optional


# OPTIMAL (Recursive DFS)
# Time: O(N), Space: O(H)
def solve_optimal(root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(node):
        nonlocal res
        if not node:
            return 0

        left_height = dfs(node.left)
        right_height = dfs(node.right)

        # Diameter passing through current node
        res = max(res, left_height + right_height)

        # Return height of the subtree rooted at current node
        return 1 + max(left_height, right_height)

    dfs(root)
    return res


# BRUTE FORCE
# The brute force would be to calculate the height of left and right subtrees for every node, leading to O(N^2) time.
def solve_brute(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    left_height = height(root.left)
    right_height = height(root.right)

    current_diameter = left_height + right_height
    left_diameter = solve_brute(root.left)
    right_diameter = solve_brute(root.right)

    return max(current_diameter, left_diameter, right_diameter)


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
        ([], 0),
    ],
)
def test_solve_optimal(arr, expected):
    root = list_to_tree(arr)
    assert solve_optimal(root) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
        ([], 0),
    ],
)
def test_solve_brute(arr, expected):
    root = list_to_tree(arr)
    assert solve_brute(root) == expected

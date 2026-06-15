"""
Problem: Validate Binary Search Tree
Difficulty: Medium
Topic: 05_trees
Companies: Amazon, Bloomberg, Meta, Microsoft, Apple

Problem Statement:
Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Complexity Proof:
- Time Complexity: O(N) since we visit every node in the tree exactly once.
- Space Complexity: O(H) where H is the height of the tree for the recursive call stack. In the worst case (skewed tree), this is O(N).
"""

import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree
from typing import Optional


# OPTIMAL (Recursive DFS with Boundaries)
# Time: O(N), Space: O(H)
def solve_optimal(root: Optional[TreeNode]) -> bool:
    def valid(node, left_bound, right_bound):
        if not node:
            return True
        if not (left_bound < node.val < right_bound):
            return False

        return valid(node.left, left_bound, node.val) and valid(
            node.right, node.val, right_bound
        )

    return valid(root, float("-inf"), float("inf"))


# BRUTE FORCE / ALTERNATIVE (Inorder Traversal)
# An inorder traversal of a valid BST will yield a strictly increasing array.
# Time: O(N), Space: O(N)
def solve_brute(root: Optional[TreeNode]) -> bool:
    res = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)

    inorder(root)

    for i in range(1, len(res)):
        if res[i] <= res[i - 1]:
            return False

    return True


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([2, 2, 2], False),
    ],
)
def test_solve_optimal(arr, expected):
    root = list_to_tree(arr)
    assert solve_optimal(root) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([2, 2, 2], False),
    ],
)
def test_solve_brute(arr, expected):
    root = list_to_tree(arr)
    assert solve_brute(root) == expected

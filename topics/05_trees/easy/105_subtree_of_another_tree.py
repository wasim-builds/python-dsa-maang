"""
Problem: Subtree of Another Tree
Difficulty: Easy
Topic: 05_trees
Companies: Amazon, Google, Microsoft, Meta, Apple

Problem Statement:
Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.
A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

Complexity Proof:
- Time Complexity: O(N * M) where N is the number of nodes in `root` and M is the number of nodes in `subRoot`. In the worst case, we might have to check if they are the "same tree" at every node in `root`. (An O(N + M) KMP string matching solution exists but is complex and rarely expected in an interview).
- Space Complexity: O(H) where H is the height of `root`, due to the recursion stack.
"""

import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree
from typing import Optional


# OPTIMAL (Recursive DFS)
# Time: O(N * M), Space: O(H)
def solve_optimal(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot:
        return True
    if not root:
        return False

    if is_same_tree(root, subRoot):
        return True

    return solve_optimal(root.left, subRoot) or solve_optimal(root.right, subRoot)


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


# BRUTE FORCE
# The standard recursive approach is essentially the brute force approach for this problem.
def solve_brute(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    return solve_optimal(root, subRoot)


@pytest.mark.parametrize(
    "arr_root, arr_sub, expected",
    [
        ([3, 4, 5, 1, 2], [4, 1, 2], True),
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
    ],
)
def test_solve_optimal(arr_root, arr_sub, expected):
    root = list_to_tree(arr_root)
    sub = list_to_tree(arr_sub)
    assert solve_optimal(root, sub) == expected


@pytest.mark.parametrize(
    "arr_root, arr_sub, expected",
    [
        ([3, 4, 5, 1, 2], [4, 1, 2], True),
    ],
)
def test_solve_brute(arr_root, arr_sub, expected):
    root = list_to_tree(arr_root)
    sub = list_to_tree(arr_sub)
    assert solve_brute(root, sub) == expected

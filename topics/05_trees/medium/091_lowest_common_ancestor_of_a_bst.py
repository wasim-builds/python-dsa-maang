"""
Problem: Lowest Common Ancestor of a Binary Search Tree
Difficulty: Medium
Topic: 05_trees
Companies: Amazon, LinkedIn, Microsoft, Facebook, Apple

Problem Statement:
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).

Complexity Proof:
- Time Complexity: O(H) where H is the height of the tree. In the worst case (skewed tree), this is O(N). In a balanced tree, this is O(log N). We only traverse one path down the tree.
- Space Complexity: O(1) for the iterative approach. O(H) for the recursive approach.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree
from typing import Optional


# BRUTE FORCE / ALTERNATIVE (Recursive)
# Time: O(H), Space: O(H)
def solve_brute(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    if not root:
        return None

    if p.val > root.val and q.val > root.val:
        return solve_brute(root.right, p, q)
    elif p.val < root.val and q.val < root.val:
        return solve_brute(root.left, p, q)
    else:
        return root


# OPTIMAL (Iterative)
# Time: O(H), Space: O(1)
def solve_optimal(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    curr = root

    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr


# Helper to find node references by value for testing
def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    if val < root.val:
        return find_node(root.left, val)
    return find_node(root.right, val)


if __name__ == "__main__":
    test_cases = [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
        ([2, 1], 2, 1, 2),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arr, p_val, q_val, expected_val in test_cases:
        root = list_to_tree(arr)
        p = find_node(root, p_val)
        q = find_node(root, q_val)
        res = solve_brute(root, p, q)
        assert res.val == expected_val
    print("All tests passed successfully!")

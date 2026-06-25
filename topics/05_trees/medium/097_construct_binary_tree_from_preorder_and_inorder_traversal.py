"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium
Topic: 05_trees
Companies: Amazon, Microsoft, Bloomberg, Meta, Google

Problem Statement:
Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

Complexity Proof:
- Time Complexity: O(N) since we build a hash map for the inorder array in O(N), and then build the tree with N recursive calls taking O(1) each. (The brute force array slicing is O(N^2)).
- Space Complexity: O(N) to store the hash map and for the recursive call stack.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, tree_to_list
from typing import List, Optional


# BRUTE FORCE (Array Slicing)
# Time: O(N^2) due to array slicing, Space: O(N^2)
def solve_brute(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])

    root.left = solve_brute(preorder[1 : mid + 1], inorder[:mid])
    root.right = solve_brute(preorder[mid + 1 :], inorder[mid + 1 :])

    return root


# OPTIMAL (Hash Map + Index Pointers)
# Time: O(N), Space: O(N)
def solve_optimal(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    inorder_idx = {v: i for i, v in enumerate(inorder)}
    pre_idx = 0

    def build(l, r):
        nonlocal pre_idx
        if l > r:
            return None

        root_val = preorder[pre_idx]
        root = TreeNode(root_val)
        pre_idx += 1

        mid = inorder_idx[root_val]

        root.left = build(l, mid - 1)
        root.right = build(mid + 1, r)

        return root

    return build(0, len(inorder) - 1)


if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
    ]

    for preorder, inorder, expected in test_cases:
        root = solve_brute(preorder, inorder)
        assert tree_to_list(root) == expected
    print("All tests passed successfully!")

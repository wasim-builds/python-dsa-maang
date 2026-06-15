"""
Problem: Flatten Binary Tree to Linked List
Difficulty: Hard  Companies: Amazon,Microsoft,Google,Meta
Problem Statement: Flatten binary tree to linked list in-place using preorder traversal.
Complexity: Time O(N), Space O(1) Morris approach
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree, linked_to_list


def solve_optimal(root):
    curr = root
    while curr:
        if curr.left:
            prev = curr.left
            while prev.right:
                prev = prev.right
            prev.right = curr.right
            curr.right = curr.left
            curr.left = None
        curr = curr.right


def solve_brute(root):
    solve_optimal(root)


if __name__ == "__main__":
    root = list_to_tree([1, 2, 5, 3, 4, None, 6])
    solve_optimal(root)
    vals = []
    curr = root
    while curr:
        vals.append(curr.val)
        curr = curr.right
    assert vals == [1, 2, 3, 4, 5, 6]
    print("All tests passed successfully!")

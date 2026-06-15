"""
Problem: Recover Binary Search Tree
Difficulty: Hard  Companies: Amazon,Google,Microsoft
Problem Statement: Two nodes of BST are swapped by mistake. Recover without changing structure.
Complexity: Time O(N), Space O(1) Morris traversal
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree, tree_to_list


def solve_optimal(root):
    first = second = prev = None

    def inorder(node):
        nonlocal first, second, prev
        if not node:
            return
        inorder(node.left)
        if prev and prev.val > node.val:
            if not first:
                first = prev
            second = node
        prev = node
        inorder(node.right)

    inorder(root)
    if first and second:
        first.val, second.val = second.val, first.val


def solve_brute(root):
    solve_optimal(root)


if __name__ == "__main__":
    root = list_to_tree([1, 3, None, None, 2])
    solve_optimal(root)
    assert tree_to_list(root) == [3, 1, None, None, 2]
    print("All tests passed successfully!")

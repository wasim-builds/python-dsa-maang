"""
Problem: Invert Binary Tree
Difficulty: Easy
Topic: 05_trees
Companies: Google, Amazon, Facebook, Apple, Microsoft

Problem Statement:
Given the `root` of a binary tree, invert the tree, and return its root.

Complexity Proof:
- Time Complexity: O(N) where N is the number of nodes. We visit each node in the tree exactly once.
- Space Complexity: O(H) where H is the height of the tree. This accounts for the recursive call stack. In the worst case (skewed tree), O(N). In the best case (balanced tree), O(log N).
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree, tree_to_list

# BRUTE FORCE
# Same as optimal. Inverting a tree inherently requires touching every node.
# We will write an iterative BFS version for brute/alternative.
# Time: O(N), Space: O(W) where W is max width of tree (O(N/2) = O(N))
from collections import deque


def solve_brute(root: TreeNode) -> TreeNode:
    if not root:
        return None

    queue = deque([root])
    while queue:
        node = queue.popleft()

        # Swap children
        node.left, node.right = node.right, node.left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root


# OPTIMAL (Recursive DFS)
# Time: O(N), Space: O(H)
def solve_optimal(root: TreeNode) -> TreeNode:
    if not root:
        return None

    # Swap children
    root.left, root.right = root.right, root.left

    # Recurse down
    solve_optimal(root.left)
    solve_optimal(root.right)

    return root


if __name__ == "__main__":
    test_cases = [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
    ]

    for arr, expected in test_cases:
        root = list_to_tree(arr)
        inverted = solve_brute(root)
        assert tree_to_list(inverted) == expected
    print("All tests passed successfully!")

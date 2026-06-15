"""
Problem: Maximum Depth of Binary Tree
Difficulty: Easy
Topic: 05_trees
Companies: Apple, LinkedIn, Amazon, Microsoft, Spotify

Problem Statement:
Given the `root` of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Complexity Proof:
- Time Complexity: O(N) where N is the number of nodes. We must visit each node once to calculate the full depth.
- Space Complexity: O(H) where H is the height of the tree. This is for the recursive call stack. In the worst case (skewed tree) this is O(N).
"""

import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree
from collections import deque


# BRUTE FORCE / ALTERNATIVE (Iterative BFS)
# Time: O(N), Space: O(W) where W is max width of tree (up to N/2)
def solve_brute(root: TreeNode) -> int:
    if not root:
        return 0

    queue = deque([root])
    depth = 0

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1

    return depth


# OPTIMAL (Recursive DFS)
# Time: O(N), Space: O(H)
def solve_optimal(root: TreeNode) -> int:
    if not root:
        return 0

    left_depth = solve_optimal(root.left)
    right_depth = solve_optimal(root.right)

    return max(left_depth, right_depth) + 1


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
    ],
)
def test_solve_optimal(arr, expected):
    root = list_to_tree(arr)
    assert solve_optimal(root) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
    ],
)
def test_solve_brute(arr, expected):
    root = list_to_tree(arr)
    assert solve_brute(root) == expected

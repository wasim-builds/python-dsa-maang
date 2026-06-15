"""
Problem: Binary Tree Level Order Traversal
Difficulty: Medium
Topic: 05_trees
Companies: Amazon, LinkedIn, Facebook, Microsoft, Apple

Problem Statement:
Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Complexity Proof:
- Time Complexity: O(N) where N is the number of nodes in the tree. We visit each node exactly once.
- Space Complexity: O(N) since the queue will hold at most N/2 nodes at the widest level of the tree (leaf level).
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree
from collections import deque
from typing import Optional, List


# OPTIMAL (Iterative BFS)
# Time: O(N), Space: O(N)
def solve_optimal(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for i in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(current_level)

    return res


# BRUTE FORCE / ALTERNATIVE (Recursive DFS keeping track of level)
# Time: O(N), Space: O(H) or O(N)
def solve_brute(root: Optional[TreeNode]) -> List[List[int]]:
    res = []

    def dfs(node, level):
        if not node:
            return

        if len(res) == level:
            res.append([])

        res[level].append(node.val)

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return res


if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
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

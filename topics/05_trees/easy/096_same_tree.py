"""
Problem: Same Tree
Difficulty: Easy
Topic: 05_trees
Companies: Amazon, Google, Microsoft, Apple, Bloomberg

Problem Statement:
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Complexity Proof:
- Time Complexity: O(N) where N is the number of nodes in the smaller of the two trees. We visit each node in both trees simultaneously.
- Space Complexity: O(H) where H is the height of the trees, due to the recursion stack. In the worst case, O(N).
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree
from collections import deque
from typing import Optional


# BRUTE FORCE / ALTERNATIVE (BFS Iterative)
# Time: O(N), Space: O(N)
def solve_brute(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    queue = deque([(p, q)])
    while queue:
        node1, node2 = queue.popleft()
        if not node1 and not node2:
            continue
        if not node1 or not node2 or node1.val != node2.val:
            return False
        queue.append((node1.left, node2.left))
        queue.append((node1.right, node2.right))
    return True


# OPTIMAL (DFS Recursive)
# Time: O(N), Space: O(H)
def solve_optimal(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False

    return solve_optimal(p.left, q.left) and solve_optimal(p.right, q.right)


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
    ]

    for arr_p, arr_q, expected in test_cases:
        p = list_to_tree(arr_p)
        q = list_to_tree(arr_q)
        assert solve_brute(p, q) == expected
    print("All tests passed successfully!")

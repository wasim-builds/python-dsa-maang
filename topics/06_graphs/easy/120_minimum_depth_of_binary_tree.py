"""
Problem: Minimum Depth of Binary Tree
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Find minimum depth from root to nearest leaf.
Complexity: Time O(N), Space O(N) BFS
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree
from collections import deque


def solve_brute(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.left:
        return 1 + solve_brute(root.right)
    if not root.right:
        return 1 + solve_brute(root.left)
    return 1 + min(solve_brute(root.left), solve_brute(root.right))


def solve_optimal(root):
    if not root:
        return 0
    q = deque([(root, 1)])
    while q:
        node, d = q.popleft()
        if not node.left and not node.right:
            return d
        if node.left:
            q.append((node.left, d + 1))
        if node.right:
            q.append((node.right, d + 1))


if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], 2),
        ([2, None, 3, None, 4, None, 5, None, 6], 5),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arr, ex in test_cases:
        assert solve_optimal(list_to_tree(arr)) == ex
    print("All tests passed successfully!")

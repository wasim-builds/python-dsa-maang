"""
Problem: Kth Smallest Element in a BST
Difficulty: Medium  Companies: Amazon,Bloomberg,Google,Meta,Microsoft
Problem Statement: Given root of BST and integer k, return kth smallest value.
Complexity: Time O(H+k), Space O(H) iterative inorder
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree


def solve_brute(root, k):
    vals = []

    def inorder(n):
        if not n:
            return
        inorder(n.left)
        vals.append(n.val)
        inorder(n.right)

    inorder(root)
    return vals[k - 1]


def solve_optimal(root, k):
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right


if __name__ == "__main__":
    test_cases = [([3, 1, 4, None, 2], 1, 1), ([5, 3, 6, 2, 4, None, None, 1], 3, 3)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arr, k, ex in test_cases:
        assert solve_optimal(list_to_tree(arr), k) == ex
    print("All tests passed successfully!")

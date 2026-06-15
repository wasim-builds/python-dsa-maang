"""
Problem: Kth Smallest Element in a BST
Difficulty: Medium  Companies: Amazon,Bloomberg,Google,Meta,Microsoft
Problem Statement: Given root of BST and integer k, return kth smallest value.
Complexity: Time O(H+k), Space O(H) iterative inorder
"""

import pytest, sys, os

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


@pytest.mark.parametrize(
    "arr,k,ex", [([3, 1, 4, None, 2], 1, 1), ([5, 3, 6, 2, 4, None, None, 1], 3, 3)]
)
def test_opt(arr, k, ex):
    assert solve_optimal(list_to_tree(arr), k) == ex

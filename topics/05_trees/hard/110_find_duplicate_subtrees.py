"""
Problem: Find Duplicate Subtrees
Difficulty: Hard  Companies: Google,Amazon,Microsoft,Facebook
Problem Statement: Return all duplicate subtrees. Two trees are duplicates if same structure and values.
Complexity: Time O(N^2) serialization, Space O(N^2)
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree
from collections import defaultdict
from typing import List, Optional


def solve_optimal(root):
    count = defaultdict(int)
    res = []

    def serialize(node):
        if not node:
            return "#"
        s = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
        count[s] += 1
        if count[s] == 2:
            res.append(node)
        return s

    serialize(root)
    return res


def solve_brute(root):
    return solve_optimal(root)


if __name__ == "__main__":
    root = list_to_tree([1, 2, 3, 4, None, 2, 4, None, None, 4])
    dups = solve_optimal(root)
    assert any((d.val == 2 for d in dups))
    print("All tests passed successfully!")

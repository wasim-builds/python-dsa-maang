"""
Problem: Binary Tree Cameras
Difficulty: Hard  Companies: Amazon,Google,Microsoft
Problem Statement: Place cameras on tree nodes such that every node is monitored. Return minimum cameras.
Complexity: Time O(N), Space O(H)
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree


def solve_optimal(root):
    res = [0]

    # 0=not covered, 1=covered no camera, 2=has camera
    def dfs(node):
        if not node:
            return 1
        l, r = dfs(node.left), dfs(node.right)
        if l == 0 or r == 0:
            res[0] += 1
            return 2
        if l == 2 or r == 2:
            return 1
        return 0

    if dfs(root) == 0:
        res[0] += 1
    return res[0]


def solve_brute(root):
    return solve_optimal(root)


if __name__ == "__main__":
    test_cases = [([0, 0, None, 0, 0], 1), ([0, 0, None, 0, None, 0, None, None, 0], 2)]

    for arr, ex in test_cases:

        def mk(arr):
            if not arr:
                return None
            from utils.data_structures import TreeNode

            nodes = [TreeNode(0) if v == 0 else None for v in (arr if arr else [])]
            if not nodes:
                return None
            for i in range(len(nodes)):
                if nodes[i] and 2 * i + 1 < len(nodes):
                    nodes[i].left = nodes[2 * i + 1]
                if nodes[i] and 2 * i + 2 < len(nodes):
                    nodes[i].right = nodes[2 * i + 2]
            return nodes[0]

        root = mk(arr)
        if root:
            assert solve_optimal(root) == ex
    print("All tests passed successfully!")

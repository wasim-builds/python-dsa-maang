"""
Problem: Serialize and Deserialize BST
Difficulty: Hard  Companies: Amazon,Google,Microsoft
Problem Statement: Design algorithm to serialize/deserialize BST more compactly than general tree.
Complexity: Time O(N), Space O(N)
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode


class Codec:
    def serialize(self, root):
        res = []

        def pre(node):
            if not node:
                return
            res.append(node.val)
            pre(node.left)
            pre(node.right)

        pre(root)
        return ",".join(map(str, res))

    def deserialize(self, data):
        if not data:
            return None
        vals = list(map(int, data.split(",")))
        idx = [0]

        def build(mn, mx):
            if idx[0] == len(vals) or not (mn < vals[idx[0]] < mx):
                return None
            val = vals[idx[0]]
            idx[0] += 1
            node = TreeNode(val)
            node.left = build(mn, val)
            node.right = build(val, mx)
            return node

        return build(float("-inf"), float("inf"))


if __name__ == "__main__":
    c = Codec()
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
    assert c.deserialize(c.serialize(root)).val == 4
    print("All tests passed successfully!")

"""
Problem: Serialize and Deserialize Binary Tree
Difficulty: Hard
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Meta,Google,Bloomberg
Problem Statement: Design algorithm to serialize/deserialize a binary tree.
Complexity: Time O(N), Space O(N)
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode
from collections import deque


class Codec:
    def serialize(self, root):
        if not root:
            return ""
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("N")
        return ",".join(res)

    def deserialize(self, data):
        if not data:
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if vals[i] != "N":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if vals[i] != "N":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root


def test_codec():
    c = Codec()
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    assert c.deserialize(c.serialize(root)).val == 1

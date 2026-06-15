"""
Common Data Structures used across all DSA problems.
Import these in any solution file.
"""
from typing import Optional, List
from collections import deque


# ─────────────────────────────────────────────
# LINKED LIST NODE
# ─────────────────────────────────────────────
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        result, node = [], self
        while node:
            result.append(str(node.val))
            node = node.next
        return " -> ".join(result)


def list_to_linked(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head


def linked_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ─────────────────────────────────────────────
# BINARY TREE NODE
# ─────────────────────────────────────────────
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def list_to_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    """Build tree from level-order list (None = missing node)."""
    if not arr or arr[0] is None:
        return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        node = queue.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Level-order traversal to list."""
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


# ─────────────────────────────────────────────
# GRAPH
# ─────────────────────────────────────────────
class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj = {}

    def add_edge(self, u, v, weight=1):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))


# ─────────────────────────────────────────────
# TRIE NODE
# ─────────────────────────────────────────────
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


# ─────────────────────────────────────────────
# UNION FIND (DSU)
# ─────────────────────────────────────────────
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

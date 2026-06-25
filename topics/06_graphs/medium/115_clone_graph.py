"""
Problem: Clone Graph
Difficulty: Medium
Topic: 06_graphs
Companies: Meta, Amazon, Microsoft, Google

Problem Statement:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Complexity Proof:
- Time Complexity: O(V + E) where V is the number of vertices (nodes) and E is the number of edges. We visit every node and every edge exactly once.
- Space Complexity: O(V) to store the hash map mapping original nodes to their clones, and for the DFS recursion stack / BFS queue.
"""

from typing import Optional


# Define the Node class for this specific problem since it's unique
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# BRUTE FORCE / ALTERNATIVE (BFS)
# Time: O(V + E), Space: O(V)
from collections import deque


def solve_brute(node: Optional["Node"]) -> Optional["Node"]:
    if not node:
        return None

    clones = {node.val: Node(node.val)}
    queue = deque([node])

    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor.val not in clones:
                clones[neighbor.val] = Node(neighbor.val)
                queue.append(neighbor)
            clones[curr.val].neighbors.append(clones[neighbor.val])

    return clones[node.val]


# OPTIMAL (DFS)
# Time: O(V + E), Space: O(V)
def solve_optimal(node: Optional["Node"]) -> Optional["Node"]:
    if not node:
        return None

    oldToNew = {}

    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]

        copy = Node(node.val)
        oldToNew[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))

        return copy

    return dfs(node)


# Helper for testing
def build_graph(adjList):
    if not adjList:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adjList))}
    for i, neighbors in enumerate(adjList):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def serialize_graph(node):
    if not node:
        return []
    visited = set()
    res = {}

    def dfs(curr):
        if curr.val in visited:
            return
        visited.add(curr.val)
        res[curr.val] = [n.val for n in curr.neighbors]
        for n in curr.neighbors:
            dfs(n)

    dfs(node)

    # Format to match input adjList style
    output = []
    for i in range(1, len(res) + 1):
        output.append(res.get(i, []))
    return output


if __name__ == "__main__":
    test_cases = [[[2, 4], [1, 3], [2, 4], [1, 3]], [[]], []]

    for adjList in test_cases:
        node = build_graph(adjList)
        cloned = solve_brute(node)
        if node:
            assert cloned is not node
        assert serialize_graph(cloned) == adjList
    print("All tests passed successfully!")

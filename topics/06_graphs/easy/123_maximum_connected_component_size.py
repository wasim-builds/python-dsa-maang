"""
Problem: Find if Path Exists in Graph
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Given n nodes and edges, determine if path exists from source to destination.
Complexity: Time O(V+E), Space O(V)
"""

from typing import List


def solve_brute(n, edges, src, dst):
    adj = {i: [] for i in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    visited = set()

    def dfs(node):
        if node == dst:
            return True
        visited.add(node)
        return any(dfs(nei) for nei in adj[node] if nei not in visited)

    return dfs(src)


def solve_optimal(n, edges, src, dst):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        parent[find(x)] = find(y)

    for a, b in edges:
        union(a, b)
    return find(src) == find(dst)


if __name__ == "__main__":
    test_cases = [
        (3, [[0, 1], [1, 2], [2, 0]], 0, 2, True),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5, False),
    ]

    for n, e, s, d, ex in test_cases:
        assert solve_optimal(n, e, s, d) == ex
    print("All tests passed successfully!")

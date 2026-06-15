"""
Problem: Graph Valid Tree
Difficulty: Easy  Companies: LinkedIn,Google,Amazon,Microsoft
Problem Statement: Given n nodes and edges, determine if they form a valid tree (connected, no cycles).
Complexity: Time O(V+E), Space O(V)
"""

from typing import List


def solve_brute(n, edges):
    if len(edges) != n - 1:
        return False
    adj = {i: [] for i in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for nei in adj[node]:
            if nei == parent:
                continue
            if nei in visited:
                return False
            if not dfs(nei, node):
                return False
        return True

    return dfs(0, -1) and len(visited) == n


def solve_optimal(n, edges):
    return solve_brute(n, edges)


if __name__ == "__main__":
    test_cases = [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for n, e, ex in test_cases:
        assert solve_optimal(n, e) == ex
    print("All tests passed successfully!")

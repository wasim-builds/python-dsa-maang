"""
Problem: Graph Bipartite Check
Difficulty: Hard  Companies: Amazon,Google,Meta
Problem Statement: Check if graph is bipartite (can be colored with 2 colors).
Complexity: Time O(V+E), Space O(V)
"""

from typing import List
from collections import deque


def solve_brute(graph):
    n = len(graph)
    color = [-1] * n

    def bfs(src):
        q = deque([src])
        color[src] = 0
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if color[nei] == -1:
                    color[nei] = 1 - color[node]
                    q.append(nei)
                elif color[nei] == color[node]:
                    return False
        return True

    return all(bfs(i) for i in range(n) if color[i] == -1)


def solve_optimal(graph):
    return solve_brute(graph)


if __name__ == "__main__":
    test_cases = [
        ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
        ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
    ]

    for g, ex in test_cases:
        assert solve_optimal(g) == ex
    print("All tests passed successfully!")

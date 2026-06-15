"""
Problem: All Paths From Source to Target
Difficulty: Medium  Companies: Google,Amazon,Facebook
Problem Statement: Find all paths from node 0 to node n-1 in a DAG.
Complexity: Time O(2^N * N), Space O(2^N * N)
"""

import pytest
from typing import List


def solve_brute(graph):
    res = []
    n = len(graph)

    def dfs(node, path):
        if node == n - 1:
            res.append(list(path))
            return
        for nei in graph[node]:
            path.append(nei)
            dfs(nei, path)
            path.pop()

    dfs(0, [0])
    return res


def solve_optimal(graph):
    return solve_brute(graph)


@pytest.mark.parametrize(
    "g,ex",
    [
        ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
        (
            [[4, 3, 1], [3, 2, 4], [3], [4], []],
            [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]],
        ),
    ],
)
def test_opt(g, ex):
    assert sorted(solve_optimal(g)) == sorted(ex)

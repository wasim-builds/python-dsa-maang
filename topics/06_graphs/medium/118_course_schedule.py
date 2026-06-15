"""
Problem: Course Schedule
Difficulty: Medium
Topic: 06_graphs
Companies: Amazon, Google, Meta, Microsoft, Apple

Problem Statement:
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`.
You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.
Return `true` if you can finish all courses. Otherwise, return `false`.

Complexity Proof:
- Time Complexity: O(V + E) where V is the number of courses (vertices) and E is the number of prerequisites (edges). We traverse the entire graph using DFS/BFS.
- Space Complexity: O(V + E) to build the adjacency list mapping courses to their prerequisites, plus the recursion stack or queue space.
"""

import pytest
from typing import List
from collections import defaultdict, deque


# OPTIMAL (Topological Sort DFS)
# Time: O(V + E), Space: O(V + E)
def solve_optimal(numCourses: int, prerequisites: List[List[int]]) -> bool:
    preMap = {i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    visitSet = set()  # all courses along the current DFS path

    def dfs(crs):
        if crs in visitSet:
            return False  # Cycle detected
        if preMap[crs] == []:
            return True  # Fully resolved

        visitSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False

        visitSet.remove(crs)
        preMap[crs] = []  # optimization: memoize that this course can be completed
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False

    return True


# BRUTE FORCE / ALTERNATIVE (Kahn's Algorithm BFS)
# Time: O(V + E), Space: O(V + E)
def solve_brute(numCourses: int, prerequisites: List[List[int]]) -> bool:
    indegree = [0] * numCourses
    adj = {i: [] for i in range(numCourses)}

    for crs, pre in prerequisites:
        adj[pre].append(crs)
        indegree[crs] += 1

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    completed = 0

    while queue:
        crs = queue.popleft()
        completed += 1
        for neighbor in adj[crs]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return completed == numCourses


@pytest.mark.parametrize(
    "numCourses, prerequisites, expected",
    [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]], True),
    ],
)
def test_solve_optimal(numCourses, prerequisites, expected):
    assert solve_optimal(numCourses, prerequisites) == expected


@pytest.mark.parametrize(
    "numCourses, prerequisites, expected",
    [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]], True),
    ],
)
def test_solve_brute(numCourses, prerequisites, expected):
    assert solve_brute(numCourses, prerequisites) == expected

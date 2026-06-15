"""
Problem: Number of Provinces
Difficulty: Easy  Companies: Amazon,Google,Microsoft,Bloomberg
Problem Statement: Given n cities and isConnected matrix, find number of provinces.
Complexity: Time O(N^2), Space O(N)
"""

from typing import List


def solve_brute(isConnected):
    n = len(isConnected)
    visited = [False] * n
    count = 0

    def dfs(i):
        for j in range(n):
            if isConnected[i][j] == 1 and not visited[j]:
                visited[j] = True
                dfs(j)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            count += 1
    return count


def solve_optimal(isConnected):
    return solve_brute(isConnected)


if __name__ == "__main__":
    test_cases = [
        ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for m, ex in test_cases:
        assert solve_optimal(m) == ex
    print("All tests passed successfully!")

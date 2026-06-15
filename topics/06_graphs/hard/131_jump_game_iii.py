"""
Problem: Jump Game III
Difficulty: Hard  Companies: Amazon,Google,Facebook
Problem Statement: Starting at index start, jump to i+arr[i] or i-arr[i]. Can you reach any index with value 0?
Complexity: Time O(N), Space O(N)
"""

import pytest
from typing import List
from collections import deque


def solve_brute(arr, start):
    n = len(arr)
    visited = set()

    def dfs(i):
        if i < 0 or i >= n or i in visited:
            return False
        if arr[i] == 0:
            return True
        visited.add(i)
        return dfs(i + arr[i]) or dfs(i - arr[i])

    return dfs(start)


def solve_optimal(arr, start):
    n = len(arr)
    q = deque([start])
    visited = set([start])
    while q:
        i = q.popleft()
        if arr[i] == 0:
            return True
        for ni in [i + arr[i], i - arr[i]]:
            if 0 <= ni < n and ni not in visited:
                visited.add(ni)
                q.append(ni)
    return False


@pytest.mark.parametrize(
    "arr,s,ex",
    [
        ([4, 2, 3, 0, 3, 1, 2], 5, True),
        ([4, 2, 3, 0, 3, 1, 2], 0, True),
        ([3, 0, 2, 1, 2], 2, False),
    ],
)
def test_opt(arr, s, ex):
    assert solve_optimal(arr, s) == ex

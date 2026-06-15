"""
Problem: Minimum Interval to Include Each Query
Difficulty: Hard  Companies: Google,Amazon,Meta
Problem Statement: For each query, find minimum-length interval containing it.
Complexity: Time O((N+Q) log N), Space O(N+Q)
"""

import pytest, heapq
from typing import List


def solve_brute(intervals, queries):
    return solve_optimal(intervals, queries)


def solve_optimal(intervals, queries):
    intervals.sort()
    q_idx = sorted(range(len(queries)), key=lambda i: queries[i])
    res = [-1] * len(queries)
    heap = []
    i = 0
    for qi in q_idx:
        q = queries[qi]
        while i < len(intervals) and intervals[i][0] <= q:
            l, r = intervals[i]
            heapq.heappush(heap, (r - l + 1, r))
            i += 1
        while heap and heap[0][1] < q:
            heapq.heappop(heap)
        if heap:
            res[qi] = heap[0][0]
    return res


@pytest.mark.parametrize(
    "inv,q,ex",
    [
        ([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5], [3, 3, 1, 4]),
        ([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22], [2, -1, 4, 6]),
    ],
)
def test_opt(inv, q, ex):
    assert solve_optimal(inv, q) == ex

"""
Problem: Network Delay Time
Difficulty: Hard  Companies: Google,Amazon,Facebook,Bloomberg
Problem Statement: Given edges with weights, find min time for signal to reach all nodes.
Complexity: Time O((V+E) log V) Dijkstra, Space O(V+E)
"""

import pytest
from typing import List
import heapq
from collections import defaultdict


def solve_brute(times, n, k):
    adj = defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))
    dist = {i: float("inf") for i in range(1, n + 1)}
    dist[k] = 0
    pq = [(0, k)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    mx = max(dist.values())
    return mx if mx < float("inf") else -1


def solve_optimal(times, n, k):
    return solve_brute(times, n, k)


@pytest.mark.parametrize(
    "t,n,k,ex",
    [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[1, 2, 1]], 2, 1, 1),
        ([[1, 2, 1]], 2, 2, -1),
    ],
)
def test_opt(t, n, k, ex):
    assert solve_optimal(t, n, k) == ex

"""
Problem: Total Cost to Hire K Workers
Difficulty: Easy  Companies: Amazon,Google,Meta
Problem Statement: Hire k workers with minimum cost. Each round hire from first/last candidates workers.
Complexity: Time O((k+candidates)*log(candidates)), Space O(candidates)
"""

import pytest, heapq
from typing import List


def solve_brute(costs, k, cands):
    res = 0
    for _ in range(k):
        pool = costs[:cands] + costs[max(cands, len(costs) - cands) :]
        mn = min(pool)
        idx = costs.index(mn)
        if idx >= len(costs) - cands and idx >= cands:
            idx = (
                len(costs)
                - 1
                - list(reversed(costs[max(cands, len(costs) - cands) :])).index(mn)
            )
        res += costs.pop(idx)
    return res


def solve_optimal(costs, k, cands):
    n = len(costs)
    heap = []
    l = 0
    r = n - 1
    for _ in range(min(cands, n)):
        heapq.heappush(heap, (costs[l], l))
        l += 1
    for i in range(n - 1, max(n - cands - 1, l - 1), -1):
        heapq.heappush(heap, (costs[i], i))
        r = i - 1
    res = 0
    for _ in range(k):
        cost, idx = heapq.heappop(heap)
        res += cost
        if l <= r:
            if idx < l:
                heapq.heappush(heap, (costs[l], l))
                l += 1
            else:
                heapq.heappush(heap, (costs[r], r))
                r -= 1
    return res


@pytest.mark.parametrize(
    "c,k,cands,ex",
    [([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4, 11), ([1, 2, 4, 1], 3, 3, 4)],
)
def test_opt(c, k, cands, ex):
    assert solve_optimal(c[:], k, cands) == ex

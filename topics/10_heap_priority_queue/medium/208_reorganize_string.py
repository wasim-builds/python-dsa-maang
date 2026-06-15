"""
Problem: Reorganize String
Difficulty: Medium  Companies: Google,Amazon,Facebook,Microsoft
Problem Statement: Rearrange characters so no two adjacent are same. Return "" if impossible.
Complexity: Time O(N log N), Space O(N)
"""

import pytest, heapq
from collections import Counter


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    count = Counter(s)
    heap = [(-cnt, c) for c, cnt in count.items()]
    heapq.heapify(heap)
    res = []
    prev = None
    while heap:
        cnt, c = heapq.heappop(heap)
        if prev and prev[0] < 0:
            heapq.heappush(heap, prev)
        res.append(c)
        cnt += 1
        prev = (cnt, c) if cnt != 0 else None
    return "".join(res) if len(res) == len(s) else ""


@pytest.mark.parametrize("s,possible", [("aab", True), ("aaab", False)])
def test_opt(s, possible):
    r = solve_optimal(s)
    if possible:
        assert r and all(r[i] != r[i + 1] for i in range(len(r) - 1))
    else:
        assert r == ""

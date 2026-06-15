"""
Problem: Reorganize String
Difficulty: Medium  Companies: Google,Amazon,Facebook,Microsoft
Problem Statement: Rearrange characters so no two adjacent are same. Return "" if impossible.
Complexity: Time O(N log N), Space O(N)
"""

import heapq
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


if __name__ == "__main__":
    test_cases = [("aab", True), ("aaab", False)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s, possible in test_cases:
        r = solve_optimal(s)
        if possible:
            assert r and all((r[i] != r[i + 1] for i in range(len(r) - 1)))
        else:
            assert r == ""
    print("All tests passed successfully!")

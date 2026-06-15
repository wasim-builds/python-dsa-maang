"""
Problem: IPO
Difficulty: Medium  Companies: Google,Amazon,Facebook
Problem Statement: Maximize capital by choosing up to k projects with initial capital w.
Complexity: Time O(N log N), Space O(N)
"""

import heapq
from typing import List


def solve_brute(k, w, profits, capital):
    n = len(profits)
    done = [False] * n
    for _ in range(k):
        best = -1
        for i in range(n):
            if (
                not done[i]
                and capital[i] <= w
                and (best == -1 or profits[i] > profits[best])
            ):
                best = i
        if best == -1:
            break
        w += profits[best]
        done[best] = True
    return w


def solve_optimal(k, w, profits, capital):
    projects = sorted(zip(capital, profits))
    heap = []
    i = 0
    for _ in range(k):
        while i < len(projects) and projects[i][0] <= w:
            heapq.heappush(heap, -projects[i][1])
            i += 1
        if not heap:
            break
        w -= heapq.heappop(heap)
    return w


if __name__ == "__main__":
    test_cases = [(2, 0, [1, 2, 3], [0, 1, 1], 4), (3, 0, [1, 2, 3], [0, 1, 2], 6)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for k, w, p, c, ex in test_cases:
        assert solve_optimal(k, w, p, c) == ex
    print("All tests passed successfully!")

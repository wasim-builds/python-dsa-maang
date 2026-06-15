"""
Problem: Single-Threaded CPU
Difficulty: Medium  Companies: Amazon,Google
Problem Statement: Return order in which CPU processes tasks (single-threaded, shortest remaining time first).
Complexity: Time O(N log N), Space O(N)
"""

import heapq
from typing import List


def solve_brute(tasks):
    return solve_optimal(tasks)


def solve_optimal(tasks):
    n = len(tasks)
    idx_tasks = sorted(range(n), key=lambda i: tasks[i][0])
    heap = []
    time = 0
    res = []
    i = 0
    while len(res) < n:
        while i < n and tasks[idx_tasks[i]][0] <= time:
            t = idx_tasks[i]
            heapq.heappush(heap, (tasks[t][1], t))
            i += 1
        if not heap:
            time = tasks[idx_tasks[i]][0]
            continue
        proc, idx = heapq.heappop(heap)
        time += proc
        res.append(idx)
    return res


if __name__ == "__main__":
    test_cases = [
        ([[1, 2], [2, 4], [3, 2], [4, 1]], [0, 2, 3, 1]),
        ([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]], [4, 3, 2, 0, 1]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for tasks, ex in test_cases:
        assert solve_optimal(tasks) == ex
    print("All tests passed successfully!")

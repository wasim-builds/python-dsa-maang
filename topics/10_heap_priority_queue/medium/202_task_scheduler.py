"""
Problem: Task Scheduler
Difficulty: Medium
Topic: 10_heap_priority_queue
Companies: Meta, Amazon, Google, Uber, Apple

Problem Statement:
Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer `n` that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least `n` units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.

Complexity Proof:
- Time Complexity: O(T) where T is the total number of tasks. We process the counts and iterate through the heap. Since the heap size is bounded by 26 (the alphabet), operations are O(1).
- Space Complexity: O(1) because the hash map and heap will hold at most 26 elements.
"""

import pytest
from typing import List
from collections import Counter, deque
import heapq


# OPTIMAL (Max Heap + Queue)
# Time: O(T), Space: O(1)
def solve_optimal(tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    # Python has no max heap, so use min heap with negative values
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    q = deque()  # pairs of [-cnt, idleTimeWhenAvailable]

    while maxHeap or q:
        time += 1

        if maxHeap:
            cnt = 1 + heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt, time + n])

        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])

    return time


# ALTERNATIVE OPTIMAL (Math formula based on max frequency)
# Time: O(T), Space: O(1)
def solve_brute(tasks: List[str], n: int) -> int:
    counts = list(Counter(tasks).values())
    max_count = max(counts)

    # Calculate how many tasks have the max_count
    max_count_tasks = counts.count(max_count)

    # Mathematical calculation of idle slots needed
    return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)


@pytest.mark.parametrize(
    "tasks, n, expected",
    [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "A", "A", "B", "B", "B"], 0, 6),
        (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
    ],
)
def test_solve_optimal(tasks, n, expected):
    assert solve_optimal(tasks, n) == expected


@pytest.mark.parametrize(
    "tasks, n, expected",
    [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "A", "A", "B", "B", "B"], 0, 6),
        (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
    ],
)
def test_solve_brute(tasks, n, expected):
    assert solve_brute(tasks, n) == expected

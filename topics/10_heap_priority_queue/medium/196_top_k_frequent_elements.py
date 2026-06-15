"""
Problem: Top K Frequent Elements
Difficulty: Medium
Topic: 10_heap_priority_queue
Companies: Amazon, Meta, Google, Microsoft, Apple

Problem Statement:
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

Complexity Proof:
- Time Complexity: O(N) using bucket sort approach, since we iterate through the array to count frequencies, and then iterate through the bucket arrays. (Alternatively O(N log k) using a heap).
- Space Complexity: O(N) because the hash map and the bucket array will store at most N unique elements.
"""

import pytest
from typing import List
from collections import Counter
import heapq


# BRUTE FORCE / ALTERNATIVE (Heap)
# Time: O(N log k), Space: O(N)
def solve_brute(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    # nlargest uses a min-heap under the hood of size k
    return heapq.nlargest(k, count.keys(), key=count.get)


# OPTIMAL (Bucket Sort)
# Time: O(N), Space: O(N)
def solve_optimal(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    return res


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
    ],
)
def test_solve_optimal(nums, k, expected):
    assert sorted(solve_optimal(nums, k)) == sorted(expected)


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
    ],
)
def test_solve_brute(nums, k, expected):
    assert sorted(solve_brute(nums, k)) == sorted(expected)

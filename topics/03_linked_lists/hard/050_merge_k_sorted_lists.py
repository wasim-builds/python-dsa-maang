"""
Problem: Merge k Sorted Lists
Difficulty: Hard
Topic: 03_linked_lists
Companies: Amazon, Microsoft, Facebook, Google, Bloomberg

Problem Statement:
You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Complexity Proof:
- Time Complexity: O(N log k) where N is the total number of nodes across all k lists. We use a priority queue of size k to always find the minimum node in O(log k) time.
- Space Complexity: O(k) for the priority queue which stores at most k nodes at any time. (Excluding the output list).
"""

import sys
import os
import heapq

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list
from typing import List, Optional


# BRUTE FORCE (Put all nodes in an array, sort, and rebuild list)
# Time: O(N log N), Space: O(N)
def solve_brute(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    nodes = []
    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next

    nodes.sort()

    dummy = ListNode(0)
    curr = dummy
    for val in nodes:
        curr.next = ListNode(val)
        curr = curr.next

    return dummy.next


# OPTIMAL (Priority Queue / Min-Heap)
# Time: O(N log k), Space: O(k)
def solve_optimal(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # We need a wrapper to break ties if values are equal because ListNode doesn't support <
    # We'll just push (val, index_in_lists, node) to the heap
    minHeap = []

    for i, l in enumerate(lists):
        if l:
            heapq.heappush(minHeap, (l.val, i, l))

    dummy = ListNode()
    curr = dummy

    while minHeap:
        val, i, node = heapq.heappop(minHeap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(minHeap, (node.next.val, i, node.next))

    return dummy.next


if __name__ == "__main__":
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arrs, expected in test_cases:
        lists = [list_to_linked(arr) for arr in arrs]
        assert linked_to_list(solve_brute(lists)) == expected
    print("All tests passed successfully!")

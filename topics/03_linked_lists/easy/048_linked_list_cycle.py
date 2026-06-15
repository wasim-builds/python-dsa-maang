"""
Problem: Linked List Cycle
Difficulty: Easy
Topic: 03_linked_lists
Companies: Amazon, Microsoft, Apple, Google, Bloomberg

Problem Statement:
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.
Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

Complexity Proof:
- Time Complexity: O(N) where N is the number of nodes. The fast pointer will catch the slow pointer in at most N steps if a cycle exists.
- Space Complexity: O(1) because we only use two pointers (`slow` and `fast`).
"""

import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked


# BRUTE FORCE
# Time: O(N), Space: O(N)
def solve_brute(head: ListNode) -> bool:
    visited = set()
    curr = head
    while curr:
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next
    return False


# OPTIMAL (Floyd's Tortoise and Hare)
# Time: O(N), Space: O(1)
def solve_optimal(head: ListNode) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


# Helper for testing
def create_cycle(arr, pos):
    head = list_to_linked(arr)
    if pos == -1 or not head:
        return head

    curr = head
    cycle_node = None
    tail = None
    idx = 0

    while curr:
        if idx == pos:
            cycle_node = curr
        tail = curr
        curr = curr.next
        idx += 1

    if tail and cycle_node:
        tail.next = cycle_node

    return head


@pytest.mark.parametrize(
    "arr, pos, expected",
    [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
    ],
)
def test_solve_optimal(arr, pos, expected):
    head = create_cycle(arr, pos)
    assert solve_optimal(head) == expected


@pytest.mark.parametrize(
    "arr, pos, expected",
    [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
    ],
)
def test_solve_brute(arr, pos, expected):
    head = create_cycle(arr, pos)
    assert solve_brute(head) == expected

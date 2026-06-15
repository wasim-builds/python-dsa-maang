"""
Problem: Linked List Cycle II
Difficulty: Hard
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Meta,Bloomberg
Problem Statement: Given linked list, return node where cycle begins, or null.
Complexity: Time O(N), Space O(1) Floyd's algorithm
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode


def solve_optimal(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow2 = head
            while slow != slow2:
                slow = slow.next
                slow2 = slow2.next
            return slow
    return None


def test_cycle_ii():
    nodes = [ListNode(i) for i in [3, 2, 0, -4]]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    nodes[-1].next = nodes[1]
    assert solve_optimal(nodes[0]) is nodes[1]

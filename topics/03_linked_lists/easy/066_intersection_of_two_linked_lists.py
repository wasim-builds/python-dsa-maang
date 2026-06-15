"""
Problem: Intersection of Two Linked Lists
Difficulty: Easy
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Bloomberg,Meta
Problem Statement: Return node at which two linked lists intersect, or null.
Complexity: Time O(M+N), Space O(1)
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode
from typing import Optional


def solve_brute(headA, headB):
    seen = set()
    while headA:
        seen.add(id(headA))
        headA = headA.next
    while headB:
        if id(headB) in seen:
            return headB
        headB = headB.next
    return None


def solve_optimal(headA, headB):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a


def test_intersection():
    shared = ListNode(8, ListNode(4, ListNode(5)))
    headA = ListNode(4, ListNode(1, shared))
    headB = ListNode(5, ListNode(6, ListNode(1, shared)))
    assert solve_optimal(headA, headB) is shared

"""
Problem: Merge Two Sorted Lists
Difficulty: Easy
Companies: Amazon, Microsoft, Google

Problem Statement:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. Return the head of the merged linked list.

Complexity Proof:
- Time Complexity: O(N + M) where N and M are the lengths of the two lists. In the worst case, we iterate until we exhaust both lists.
- Space Complexity: O(1) because we only allocate a dummy node and a few pointers. We reuse the existing nodes from the input lists.
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list
import pytest


# OPTIMAL
# Time: O(n + m), Space: O(1)
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ],
)
def test_mergeTwoLists(list1, list2, expected):
    l1 = list_to_linked(list1)
    l2 = list_to_linked(list2)
    merged = mergeTwoLists(l1, l2)
    assert linked_to_list(merged) == expected

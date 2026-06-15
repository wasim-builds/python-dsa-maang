"""
Problem: Delete Node in a Linked List
Difficulty: Easy
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Adobe
Problem Statement: Delete a node given only access to that node (not head). Node is not tail.
Complexity: Time O(1), Space O(1)
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list


def solve_optimal(node):
    node.val = node.next.val
    node.next = node.next.next


def solve_brute(node):
    solve_optimal(node)


def test_delete_node():
    head = list_to_linked([4, 5, 1, 9])
    node = head.next
    solve_optimal(node)
    assert linked_to_list(head) == [4, 1, 9]

"""
Problem: Middle of the Linked List
Difficulty: Easy
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Apple
Problem Statement: Given head, return the middle node. If two middles return second.
Complexity: Time O(N), Space O(1)
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list


def solve_brute(head):
    nodes = []
    while head:
        nodes.append(head)
        head = head.next
    return nodes[len(nodes) // 2]


def solve_optimal(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


@pytest.mark.parametrize(
    "arr,ex", [([1, 2, 3, 4, 5], [3, 4, 5]), ([1, 2, 3, 4, 5, 6], [4, 5, 6])]
)
def test_opt(arr, ex):
    assert linked_to_list(solve_optimal(list_to_linked(arr))) == ex

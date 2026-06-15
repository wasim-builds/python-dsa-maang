"""
Problem: Swap Nodes in Pairs
Difficulty: Medium
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Bloomberg
Problem Statement: Swap every two adjacent nodes and return its head. Must not modify values.
Complexity: Time O(N), Space O(1)
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list


def solve_brute(head):
    dummy = ListNode(0, head)
    prev = dummy
    while prev.next and prev.next.next:
        a, b = prev.next, prev.next.next
        prev.next = b
        a.next = b.next
        b.next = a
        prev = a
    return dummy.next


def solve_optimal(head):
    return solve_brute(head)


@pytest.mark.parametrize("arr,ex", [([1, 2, 3, 4], [2, 1, 4, 3]), ([], []), ([1], [1])])
def test_opt(arr, ex):
    assert linked_to_list(solve_optimal(list_to_linked(arr))) == ex

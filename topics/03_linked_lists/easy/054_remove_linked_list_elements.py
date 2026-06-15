"""
Problem: Remove Linked List Elements
Difficulty: Easy
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Google
Problem Statement: Remove all nodes with value val. Return new head.
Complexity: Time O(N), Space O(1)
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list


def solve_brute(head, val):
    dummy = ListNode(0, head)
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next


def solve_optimal(head, val):
    return solve_brute(head, val)


@pytest.mark.parametrize(
    "arr,val,ex",
    [([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]), ([], 1, []), ([7, 7, 7, 7], 7, [])],
)
def test_opt(arr, val, ex):
    assert linked_to_list(solve_optimal(list_to_linked(arr), val)) == ex

"""
Problem: Reorder List
Difficulty: Medium
Topic: 03_linked_lists  Companies: Amazon,Google,Meta,Microsoft
Problem Statement: Given list L0→L1→…→Ln, reorder to L0→Ln→L1→Ln-1→…
Complexity: Time O(N), Space O(1)
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list


def solve_optimal(head):
    if not head:
        return
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None
    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2


def solve_brute(head):
    solve_optimal(head)


@pytest.mark.parametrize(
    "arr,ex", [([1, 2, 3, 4], [1, 4, 2, 3]), ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3])]
)
def test_opt(arr, ex):
    h = list_to_linked(arr)
    solve_optimal(h)
    assert linked_to_list(h) == ex

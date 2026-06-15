"""
Problem: Palindrome Linked List
Difficulty: Easy
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Meta,Bloomberg
Problem Statement: Given head of linked list, return true if it is a palindrome.
Complexity: Time O(N), Space O(1) using fast/slow pointer + reverse
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list


def solve_brute(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals == vals[::-1]


def solve_optimal(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    l, r = head, prev
    while r:
        if l.val != r.val:
            return False
        l = l.next
        r = r.next
    return True


@pytest.mark.parametrize("arr,ex", [([1, 2, 2, 1], True), ([1, 2], False)])
def test_opt(arr, ex):
    assert solve_optimal(list_to_linked(arr)) == ex

"""
Problem: Add Two Numbers
Difficulty: Medium
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Bloomberg,Meta,Apple
Problem Statement: Two non-empty linked lists represent two non-negative integers in reverse order. Return sum as linked list.
Complexity: Time O(max(M,N)), Space O(max(M,N))
"""

import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list


def solve_brute(l1, l2):
    n1 = n2 = 0
    i = 0
    while l1:
        n1 += l1.val * (10**i)
        l1 = l1.next
        i += 1
    i = 0
    while l2:
        n2 += l2.val * (10**i)
        l2 = l2.next
        i += 1
    return list_to_linked([int(d) for d in str(n1 + n2)[::-1]])


def solve_optimal(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        s = v1 + v2 + carry
        carry = s // 10
        curr.next = ListNode(s % 10)
        curr = curr.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next


@pytest.mark.parametrize(
    "a,b,ex",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_opt(a, b, ex):
    assert linked_to_list(solve_optimal(list_to_linked(a), list_to_linked(b))) == ex

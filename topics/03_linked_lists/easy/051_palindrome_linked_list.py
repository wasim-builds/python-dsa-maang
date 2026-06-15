"""
Problem: Palindrome Linked List
Difficulty: Easy
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Meta,Bloomberg
Problem Statement: Given head of linked list, return true if it is a palindrome.
Complexity: Time O(N), Space O(1) using fast/slow pointer + reverse
"""

import sys, os

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


if __name__ == "__main__":
    test_cases = [([1, 2, 2, 1], True), ([1, 2], False)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arr, ex in test_cases:
        assert solve_optimal(list_to_linked(arr)) == ex
    print("All tests passed successfully!")

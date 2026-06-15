"""
Problem: Reverse Linked List
Difficulty: Easy
Companies: Amazon, Microsoft, Apple, Google

Problem Statement:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Complexity Proof:
- Time Complexity: O(N) where N is the number of nodes in the linked list. We visit each node exactly once.
- Space Complexity: O(1) because we only use three pointers (`prev`, `curr`, `nxt`) to reverse the links in place.
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list


# OPTIMAL (Iterative)
# Time: O(n), Space: O(1)
def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), ([1, 2], [2, 1]), ([], [])]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for input_list, expected in test_cases:
        head = list_to_linked(input_list)
        rev_head = reverseList(head)
        assert linked_to_list(rev_head) == expected
    print("All tests passed successfully!")

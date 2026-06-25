"""
Problem: Remove Nth Node From End of List
Difficulty: Medium
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Bloomberg,Apple
Problem Statement: Remove the nth node from the end of the list and return its head.
Complexity: Time O(N), Space O(1) two-pointer
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list


def solve_brute(head, n):
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    idx = len(nodes) - n
    if idx == 0:
        return head.next
    nodes[idx - 1].next = nodes[idx].next
    return head


def solve_optimal(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head
    for _ in range(n):
        right = right.next
    while right:
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]), ([1], 1, []), ([1, 2], 1, [1])]

    for arr, n, ex in test_cases:
        assert linked_to_list(solve_optimal(list_to_linked(arr), n)) == ex
    print("All tests passed successfully!")

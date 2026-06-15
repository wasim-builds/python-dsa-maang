"""
Problem: Middle of the Linked List
Difficulty: Easy
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Apple
Problem Statement: Given head, return the middle node. If two middles return second.
Complexity: Time O(N), Space O(1)
"""

import sys, os

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


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4, 5], [3, 4, 5]), ([1, 2, 3, 4, 5, 6], [4, 5, 6])]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arr, ex in test_cases:
        assert linked_to_list(solve_optimal(list_to_linked(arr))) == ex
    print("All tests passed successfully!")

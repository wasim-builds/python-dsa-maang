"""
Problem: Remove Linked List Elements
Difficulty: Easy
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Google
Problem Statement: Remove all nodes with value val. Return new head.
Complexity: Time O(N), Space O(1)
"""

import sys, os

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


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
        ([], 1, []),
        ([7, 7, 7, 7], 7, []),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arr, val, ex in test_cases:
        assert linked_to_list(solve_optimal(list_to_linked(arr), val)) == ex
    print("All tests passed successfully!")

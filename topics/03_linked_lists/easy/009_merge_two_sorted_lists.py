"""
Problem: Merge Two Sorted Lists
Difficulty: Easy
Companies: Amazon, Microsoft, Google

Problem Statement:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. Return the head of the merged linked list.

Complexity Proof:
- Time Complexity: O(N + M) where N and M are the lengths of the two lists. In the worst case, we iterate until we exhaust both lists.
- Space Complexity: O(1) because we only allocate a dummy node and a few pointers. We reuse the existing nodes from the input lists.
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list


# OPTIMAL
# Time: O(n + m), Space: O(1)
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for list1, list2, expected in test_cases:
        l1 = list_to_linked(list1)
        l2 = list_to_linked(list2)
        merged = mergeTwoLists(l1, l2)
        assert linked_to_list(merged) == expected
    print("All tests passed successfully!")

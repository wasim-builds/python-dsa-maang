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


from typing import Optional

# OPTIMAL
# Time: O(n + m), Space: O(1)
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # A dummy node helps to easily build the new list without 
    # writing special edge case logic for the very first node.
    dummy = ListNode()
    
    # 'tail' will always point to the last node in our new merged list.
    tail = dummy

    # While both lists have nodes left to process
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1       # Link the smaller node
            list1 = list1.next      # Move the list1 pointer forward
        else:
            tail.next = list2       # Link the smaller node
            list2 = list2.next      # Move the list2 pointer forward
            
        tail = tail.next            # Move our tail pointer forward

    # If one list is exhausted but the other still has nodes,
    # simply link the remaining nodes to our tail.
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    # The actual merged list starts at dummy.next
    return dummy.next


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ]

    for list1, list2, expected in test_cases:
        l1 = list_to_linked(list1)
        l2 = list_to_linked(list2)
        merged = mergeTwoLists(l1, l2)
        assert linked_to_list(merged) == expected
    print("All tests passed successfully!")

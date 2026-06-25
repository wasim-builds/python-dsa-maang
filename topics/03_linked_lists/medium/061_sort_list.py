"""
Problem: Sort List
Difficulty: Medium
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Bloomberg,Google
Problem Statement: Sort linked list in O(n log n) time and O(1) space.
Complexity: Time O(N log N), Space O(log N) for recursion stack
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list


def solve_brute(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    vals.sort()
    return list_to_linked(vals)


def solve_optimal(head):
    if not head or not head.next:
        return head
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    L = solve_optimal(head)
    R = solve_optimal(mid)
    dummy = ListNode()
    curr = dummy
    while L and R:
        if L.val <= R.val:
            curr.next = L
            L = L.next
        else:
            curr.next = R
            R = R.next
        curr = curr.next
    curr.next = L or R
    return dummy.next


if __name__ == "__main__":
    test_cases = [([4, 2, 1, 3], [1, 2, 3, 4]), ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5])]

    for arr, ex in test_cases:
        assert linked_to_list(solve_optimal(list_to_linked(arr))) == ex
    print("All tests passed successfully!")

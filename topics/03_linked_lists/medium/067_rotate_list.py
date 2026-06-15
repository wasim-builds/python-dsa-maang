"""
Problem: Rotate List
Difficulty: Medium
Topic: 03_linked_lists  Companies: Amazon,Microsoft
Problem Statement: Rotate list to the right by k places.
Complexity: Time O(N), Space O(1)
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list


def solve_brute(head, k):
    if not head:
        return head
    vals = linked_to_list(head)
    k %= len(vals)
    return list_to_linked(vals[-k:] + vals[:-k]) if k else head


def solve_optimal(head, k):
    if not head or not head.next:
        return head
    n = 1
    tail = head
    while tail.next:
        tail = tail.next
        n += 1
    k %= n
    if k == 0:
        return head
    curr = head
    for _ in range(n - k - 1):
        curr = curr.next
    new_head = curr.next
    curr.next = None
    tail.next = head
    return new_head


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]), ([0, 1, 2], 4, [2, 0, 1])]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arr, k, ex in test_cases:
        assert linked_to_list(solve_optimal(list_to_linked(arr), k)) == ex
    print("All tests passed successfully!")

"""
Problem: Merge K Lists (Divide & Conquer variant)
Difficulty: Hard
Topic: 03_linked_lists  Companies: Amazon,Google,Microsoft
Problem Statement: Merge K sorted linked lists using divide and conquer approach.
Complexity: Time O(N log K), Space O(log K)
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list
from typing import List, Optional


def merge_two(l1, l2):
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next


def solve_optimal(lists):
    if not lists:
        return None
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(merge_two(l1, l2))
        lists = merged
    return lists[0]


if __name__ == "__main__":
    test_cases = [([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6])]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arrs, ex in test_cases:
        assert linked_to_list(solve_optimal([list_to_linked(a) for a in arrs])) == ex
    print("All tests passed successfully!")

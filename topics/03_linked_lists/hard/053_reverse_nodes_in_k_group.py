"""
Problem: Reverse Nodes in k-Group
Difficulty: Hard
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Meta,Google
Problem Statement: Reverse nodes in k-groups. If remaining nodes < k, leave them as-is.
Complexity: Time O(N), Space O(1)
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import ListNode, list_to_linked, linked_to_list


def solve_brute(head, k):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    res = []
    for i in range(0, len(vals), k):
        chunk = vals[i : i + k]
        if len(chunk) == k:
            res += chunk[::-1]
        else:
            res += chunk
    return list_to_linked(res)


def solve_optimal(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        kth = get_kth(group_prev, k)
        if not kth:
            break
        group_next = kth.next
        prev, curr = group_next, group_prev.next
        while curr != group_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp
    return dummy.next


def get_kth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
    ]

    for arr, k, ex in test_cases:
        assert linked_to_list(solve_optimal(list_to_linked(arr), k)) == ex
    print("All tests passed successfully!")

"""
Problem: Copy List with Random Pointer
Difficulty: Hard
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Meta,Bloomberg
Problem Statement: Deep copy a linked list where each node has next and random pointers.
Complexity: Time O(N), Space O(N)
"""


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random


def solve_optimal(head):
    if not head:
        return None
    m = {None: None}
    curr = head
    while curr:
        m[curr] = Node(curr.val)
        curr = curr.next
    curr = head
    while curr:
        m[curr].next = m[curr.next]
        m[curr].random = m[curr.random]
        curr = curr.next
    return m[head]


if __name__ == "__main__":
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)
    n4 = Node(10)
    n5 = Node(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n2.random = n1
    n3.random = n5
    n4.random = n3
    n5.random = n1
    copy = solve_optimal(n1)
    assert copy is not n1 and copy.val == 7 and (copy.next.val == 13)
    print("All tests passed successfully!")

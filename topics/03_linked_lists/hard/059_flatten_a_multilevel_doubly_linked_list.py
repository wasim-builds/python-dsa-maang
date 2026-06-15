"""
Problem: Flatten a Multilevel Doubly Linked List
Difficulty: Hard
Topic: 03_linked_lists  Companies: Amazon,Microsoft,Meta
Problem Statement: Flatten multilevel doubly linked list with child pointers into single level.
Complexity: Time O(N), Space O(N) for stack
"""


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def solve_optimal(head):
    if not head:
        return head
    stack = []
    curr = head
    while curr:
        if curr.child:
            if curr.next:
                stack.append(curr.next)
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
        if not curr.next and stack:
            nxt = stack.pop()
            curr.next = nxt
            nxt.prev = curr
        curr = curr.next
    return head


if __name__ == "__main__":
    n1, n2, n3 = (Node(1), Node(2), Node(3))
    n1.next = n2
    n2.prev = n1
    n2.next = n3
    n3.prev = n2
    c = Node(7)
    n2.child = c
    r = solve_optimal(n1)
    vals = []
    while r:
        vals.append(r.val)
        r = r.next
    assert vals == [1, 2, 7, 3]
    print("All tests passed successfully!")

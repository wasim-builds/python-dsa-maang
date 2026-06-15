"""
Problem: Implement Queue using Stacks
Difficulty: Easy  Companies: Amazon,Microsoft,Bloomberg
Problem Statement: Implement FIFO queue using only two stacks.
Complexity: Time O(1) amortized, Space O(N)
"""

import pytest


class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2


def test_queue():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert not q.empty()

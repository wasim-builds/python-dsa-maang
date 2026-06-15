"""
Problem: Smallest Number in Infinite Set
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Design data structure to track smallest number in initially-infinite set with add-back.
Complexity: Time O(log N) pop, O(log N) add
"""

import pytest, heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []
        self.added = set()
        self.curr = 1

    def popSmallest(self):
        if self.heap:
            v = heapq.heappop(self.heap)
            self.added.discard(v)
            return v
        v = self.curr
        self.curr += 1
        return v

    def addBack(self, n):
        if n < self.curr and n not in self.added:
            self.added.add(n)
            heapq.heappush(self.heap, n)


def test_set():
    s = SmallestInfiniteSet()
    assert s.popSmallest() == 1
    s.addBack(1)
    assert s.popSmallest() == 1
    assert s.popSmallest() == 2

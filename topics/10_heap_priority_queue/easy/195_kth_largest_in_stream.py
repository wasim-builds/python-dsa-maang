"""
Problem: Kth Largest Element in a Stream
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Design class that finds kth largest element in stream.
Complexity: Time O(log k) add, Space O(k)
"""

import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for n in nums:
            self.add(n)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    obj = KthLargest(3, [4, 5, 8, 2])
    assert obj.add(3) == 4
    assert obj.add(5) == 5
    assert obj.add(10) == 5
    assert obj.add(9) == 8
    print("All tests passed successfully!")

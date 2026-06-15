"""
Problem: Find Median from Data Stream
Difficulty: Hard
Topic: 10_heap_priority_queue
Companies: Amazon, Microsoft, Apple, Google, Meta

Problem Statement:
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
Implement the `MedianFinder` class:
- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

Complexity Proof:
- Time Complexity: O(log N) for `addNum` because pushing to and popping from a heap takes logarithmic time. O(1) for `findMedian` because we just peek at the top of the heaps.
- Space Complexity: O(N) where N is the number of elements added, as we store all elements across the two heaps.
"""

import heapq


# OPTIMAL (Two Heaps)
class MedianFinder:
    def __init__(self):
        # Two heaps:
        # small is a max-heap (implemented as min-heap with negative values) for the smaller half of numbers
        # large is a min-heap for the larger half of numbers
        self.small = []
        self.large = []

    # Time: O(log N)
    def addNum(self, num: int) -> None:
        # Default push to small (max-heap)
        heapq.heappush(self.small, -num)

        # Make sure every num in small is <= every num in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes so they differ by at most 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    # Time: O(1)
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0
    print("All tests passed successfully!")

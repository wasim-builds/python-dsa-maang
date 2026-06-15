"""
Problem: Kth Largest Element in an Array
Difficulty: Medium
Topic: 10_heap_priority_queue
Companies: Facebook, Amazon, Google, Microsoft, Apple

Problem Statement:
Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.
Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.
Can you solve it without sorting?

Complexity Proof:
- Time Complexity: O(N) average time for Quickselect, O(N^2) in the worst case. (Alternatively O(N log k) using a Min-Heap).
- Space Complexity: O(1) for Quickselect. O(k) for Min-Heap.
"""

from typing import List
import heapq
import random


# BRUTE FORCE / ALTERNATIVE (Min-Heap)
# Time: O(N log k), Space: O(k)
def solve_brute(nums: List[int], k: int) -> int:
    minHeap = []
    for num in nums:
        heapq.heappush(minHeap, num)
        if len(minHeap) > k:
            heapq.heappop(minHeap)
    return minHeap[0]


# OPTIMAL (Quickselect)
# Time: O(N) average, O(N^2) worst case, Space: O(1)
def solve_optimal(nums: List[int], k: int) -> int:
    k = len(nums) - k  # Convert to find the index in sorted array

    def quickSelect(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k:
            return quickSelect(l, p - 1)
        elif p < k:
            return quickSelect(p + 1, r)
        else:
            return nums[p]

    # Optional: shuffle nums to avoid worst-case O(N^2) for already sorted arrays
    # random.shuffle(nums)
    return quickSelect(0, len(nums) - 1)


if __name__ == "__main__":
    test_cases = [([3, 2, 1, 5, 6, 4], 2, 5), ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, k, expected in test_cases:
        assert solve_brute(nums[:], k) == expected
    print("All tests passed successfully!")

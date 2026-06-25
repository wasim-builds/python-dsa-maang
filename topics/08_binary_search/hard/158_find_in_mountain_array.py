"""
Problem: Find in Mountain Array
Difficulty: Hard  Companies: Google,Amazon
Problem Statement: Find minimum index such that arr.get(index)==target in mountain array.
Complexity: Time O(log N), Space O(1)
"""

from typing import List


class MountainArray:
    def __init__(self, arr):
        self._arr = arr

    def get(self, idx):
        return self._arr[idx]

    def length(self):
        return len(self._arr)


def solve_optimal(target, arr):
    n = arr.length()
    l, r = 0, n - 1
    while l < r:
        mid = (l + r) // 2
        if arr.get(mid) < arr.get(mid + 1):
            l = mid + 1
        else:
            r = mid
    peak = l
    l, r = 0, peak
    while l <= r:
        mid = (l + r) // 2
        v = arr.get(mid)
        if v == target:
            return mid
        elif v < target:
            l = mid + 1
        else:
            r = mid - 1
    l, r = peak, n - 1
    while l <= r:
        mid = (l + r) // 2
        v = arr.get(mid)
        if v == target:
            return mid
        elif v > target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4, 5, 3, 1], 3, 2), ([0, 1, 2, 4, 2, 1], 3, -1)]

    for arr, t, ex in test_cases:
        assert solve_optimal(t, MountainArray(arr)) == ex
    print("All tests passed successfully!")

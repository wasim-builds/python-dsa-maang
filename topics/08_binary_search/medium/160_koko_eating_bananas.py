"""
Problem: Koko Eating Bananas
Difficulty: Medium
Topic: 08_binary_search
Companies: Google, Amazon, Meta, Airbnb, Microsoft

Problem Statement:
Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.
Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.
Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

Complexity Proof:
- Time Complexity: O(N log(max(P))) where N is the number of piles and max(P) is the maximum number of bananas in a pile. The binary search takes O(log(max(P))) steps, and for each step, we iterate through the N piles to calculate the hours.
- Space Complexity: O(1) because we only use a few variables (`l`, `r`, `res`) for the binary search.
"""

import math
from typing import List


# BRUTE FORCE
# Time: O(max(P) * N), Space: O(1)
def solve_brute(piles: List[int], h: int) -> int:
    k = 1
    while True:
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        if hours <= h:
            return k
        k += 1


# OPTIMAL (Binary Search on Answer Space)
# Time: O(N * log(max(P))), Space: O(1)
def solve_optimal(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (l + r) // 2

        hours = 0
        for p in piles:
            hours += math.ceil(p / k)

        if hours <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1

    return res


# Restrict brute force to small tests to prevent timeout

if __name__ == "__main__":
    test_cases = [([3, 6, 7, 11], 8, 4)]

    for piles, h, expected in test_cases:
        assert solve_brute(piles, h) == expected
    print("All tests passed successfully!")

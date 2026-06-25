"""
Problem: Minimum Time to Complete Trips
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Binary search for minimum time such that all buses complete totalTrips.
Complexity: Time O(N log(total)), Space O(1)
"""

from typing import List


def solve_brute(time, total):
    return solve_optimal(time, total)


def solve_optimal(time, totalTrips):
    l, r = 1, min(time) * totalTrips
    while l < r:
        mid = (l + r) // 2
        if sum(mid // t for t in time) >= totalTrips:
            r = mid
        else:
            l = mid + 1
    return l


if __name__ == "__main__":
    test_cases = [([1, 2, 3], 5, 3), ([2], 1, 2)]

    for t, total, ex in test_cases:
        assert solve_optimal(t, total) == ex
    print("All tests passed successfully!")

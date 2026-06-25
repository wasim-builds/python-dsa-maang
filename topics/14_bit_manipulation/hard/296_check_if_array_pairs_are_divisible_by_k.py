"""
Problem: Check If Array Pairs Are Divisible by k
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Check if array can be paired such that sum of each pair divisible by k.
Complexity: Time O(N), Space O(k)
"""

from typing import List


def solve_brute(arr, k):
    return solve_optimal(arr, k)


def solve_optimal(arr, k):
    count = [0] * k
    for n in arr:
        count[n % k] += 1
    if count[0] % 2:
        return False
    for i in range(1, k // 2 + 1):
        if i != k - i and count[i] != count[k - i]:
            return False
        if i == k - i and count[i] % 2:
            return False
    return True


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5, True),
        ([1, 2, 3, 4, 5, 6], 10, False),
    ]

    for arr, k, ex in test_cases:
        assert solve_optimal(arr, k) == ex
    print("All tests passed successfully!")

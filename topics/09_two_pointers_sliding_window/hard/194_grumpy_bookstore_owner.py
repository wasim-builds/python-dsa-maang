"""
Problem: Grumpy Bookstore Owner
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Find max customers satisfied using 'grumpy' suppression window of size minutes.
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(customers, grumpy, minutes):
    always = sum(c for c, g in zip(customers, grumpy) if g == 0)
    best = 0
    for i in range(len(customers) - minutes + 1):
        extra = sum(
            c
            for c, g in zip(customers[i : i + minutes], grumpy[i : i + minutes])
            if g == 1
        )
        best = max(best, extra)
    return always + best


def solve_optimal(customers, grumpy, minutes):
    always = sum(c for c, g in zip(customers, grumpy) if g == 0)
    window = sum(c * g for c, g in zip(customers[:minutes], grumpy[:minutes]))
    best = window
    for i in range(minutes, len(customers)):
        window += (
            customers[i] * grumpy[i] - customers[i - minutes] * grumpy[i - minutes]
        )
        best = max(best, window)
    return always + best


if __name__ == "__main__":
    test_cases = [([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3, 16)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for c, g, m, ex in test_cases:
        assert solve_optimal(c, g, m) == ex
    print("All tests passed successfully!")

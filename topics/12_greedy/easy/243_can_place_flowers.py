"""
Problem: Can Place Flowers
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Return if n flowers can be planted in flowerbed with no adjacent.
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(f, n):
    return solve_optimal(f, n)


def solve_optimal(flowerbed, n):
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            empty_left = i == 0 or flowerbed[i - 1] == 0
            empty_right = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            if empty_left and empty_right:
                flowerbed[i] = 1
                n -= 1
    return n <= 0


if __name__ == "__main__":
    test_cases = [([1, 0, 0, 0, 1], 1, True), ([1, 0, 0, 0, 1], 2, False)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for f, n, ex in test_cases:
        assert solve_optimal(f[:], n) == ex
    print("All tests passed successfully!")

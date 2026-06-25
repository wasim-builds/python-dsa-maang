"""
Problem: Decode XORed Array
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Given encoded and first element, recover original array.
Complexity: Time O(N), Space O(N)
"""

from typing import List


def solve_brute(encoded, first):
    return solve_optimal(encoded, first)


def solve_optimal(encoded, first):
    arr = [first]
    for e in encoded:
        arr.append(arr[-1] ^ e)
    return arr


if __name__ == "__main__":
    test_cases = [([1, 2, 3], 1, [1, 0, 2, 1]), ([6, 2, 7, 3], 4, [4, 2, 0, 7, 4])]

    for enc, f, ex in test_cases:
        assert solve_optimal(enc, f) == ex
    print("All tests passed successfully!")

"""
Problem: Count Triplets That Can Form Two Arrays of Equal XOR
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Count triplets (i,j,k) where XOR(i..j-1)==XOR(j..k).
Complexity: Time O(N^2), Space O(N)
"""

from typing import List


def solve_brute(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j, n):
                a = b = 0
                for x in range(i, j):
                    a ^= arr[x]
                for x in range(j, k + 1):
                    b ^= arr[x]
                if a == b:
                    count += 1
    return count


def solve_optimal(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        xor = arr[i]
        for k in range(i + 1, n):
            xor ^= arr[k]
            if xor == 0:
                count += k - i
    return count


if __name__ == "__main__":
    test_cases = [([2, 3, 1, 6, 7], 4), ([1, 1, 1, 1, 1], 10)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arr, ex in test_cases:
        assert solve_optimal(arr) == ex
    print("All tests passed successfully!")

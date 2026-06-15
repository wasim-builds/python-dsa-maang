"""
Problem: Longest Turbulent Subarray
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Return max length subarray that is turbulent (alternating comparisons).
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(arr):
    n = len(arr)
    res = 1
    for i in range(n):
        cur = 1
        for j in range(i + 1, n):
            cmp = arr[j] - arr[j - 1]
            if j == i + 1:
                if cmp == 0:
                    break
                cur = 2
            else:
                prev = arr[j - 1] - arr[j - 2]
                if cmp * prev < 0:
                    cur += 1
                else:
                    break
        res = max(res, cur)
    return res


def solve_optimal(arr):
    res = inc = dec = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            inc = dec + 1
            dec = 1
        elif arr[i] < arr[i - 1]:
            dec = inc + 1
            inc = 1
        else:
            inc = dec = 1
        res = max(res, inc, dec)
    return res


if __name__ == "__main__":
    test_cases = [([9, 4, 2, 10, 7, 8, 8, 1, 9], 5), ([4, 8, 12, 16], 2), ([100], 1)]
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

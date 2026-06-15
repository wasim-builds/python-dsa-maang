"""
Problem: Find Smallest Letter Greater Than Target
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Find the smallest element in sorted char array strictly greater than target. Wraps around.
Complexity: Time O(log N), Space O(1)
"""

from typing import List


def solve_brute(letters, target):
    for c in letters:
        if c > target:
            return c
    return letters[0]


def solve_optimal(letters, target):
    l, r = 0, len(letters) - 1
    while l <= r:
        mid = (l + r) // 2
        if letters[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1
    return letters[l % len(letters)]


if __name__ == "__main__":
    test_cases = [
        (["c", "f", "j"], "a", "c"),
        (["c", "f", "j"], "c", "f"),
        (["c", "f", "j"], "j", "c"),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for l, t, ex in test_cases:
        assert solve_optimal(l, t) == ex
    print("All tests passed successfully!")

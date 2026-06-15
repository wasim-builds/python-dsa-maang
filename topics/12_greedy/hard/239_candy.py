"""
Problem: Candy
Difficulty: Hard  Companies: Amazon,Google,Bloomberg
Problem Statement: Give each child at least 1 candy; more than neighbors with higher rating. Return min total.
Complexity: Time O(N), Space O(N)
"""

from typing import List


def solve_brute(r):
    return solve_optimal(r)


def solve_optimal(ratings):
    n = len(ratings)
    candy = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candy[i] = candy[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candy[i] = max(candy[i], candy[i + 1] + 1)
    return sum(candy)


if __name__ == "__main__":
    test_cases = [([1, 0, 2], 5), ([1, 2, 2], 4)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for r, ex in test_cases:
        assert solve_optimal(r) == ex
    print("All tests passed successfully!")

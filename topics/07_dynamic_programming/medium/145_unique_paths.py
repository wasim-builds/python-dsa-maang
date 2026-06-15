"""
Problem: Unique Paths
Difficulty: Medium  Companies: Amazon,Google,Microsoft,Bloomberg
Problem Statement: Robot on m x n grid, can move right or down. How many paths from top-left to bottom-right?
Complexity: Time O(M*N), Space O(N)
"""


def solve_brute(m, n):
    from math import comb

    return comb(m + n - 2, n - 1)


def solve_optimal(m, n):
    dp = [1] * n
    for r in range(1, m):
        for c in range(1, n):
            dp[c] += dp[c - 1]
    return dp[n - 1]


if __name__ == "__main__":
    test_cases = [(3, 7, 28), (3, 2, 3), (1, 1, 1)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for m, n, ex in test_cases:
        assert solve_optimal(m, n) == ex
    print("All tests passed successfully!")

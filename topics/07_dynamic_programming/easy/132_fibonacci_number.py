"""
Problem: Fibonacci Number
Difficulty: Easy  Companies: Amazon,Microsoft,Apple
Problem Statement: Return the nth Fibonacci number.
Complexity: Time O(N), Space O(1)
"""


def solve_brute(n):
    if n <= 1:
        return n
    return solve_brute(n - 1) + solve_brute(n - 2)


def solve_optimal(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    test_cases = [(5, 5)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for n, ex in test_cases:
        assert solve_brute(n) == ex
    print("All tests passed successfully!")

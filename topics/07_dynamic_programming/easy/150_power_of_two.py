"""
Problem: Power of Two
Difficulty: Easy  Companies: Amazon,Microsoft,Apple
Problem Statement: Return true if n is a power of two.
Complexity: Time O(1), Space O(1)
"""


def solve_brute(n):
    return n > 0 and (n & (n - 1)) == 0


def solve_optimal(n):
    return n > 0 and not (n & (n - 1))


if __name__ == "__main__":
    test_cases = [(1, True), (16, True), (3, False), (0, False)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for n, ex in test_cases:
        assert solve_optimal(n) == ex
    print("All tests passed successfully!")

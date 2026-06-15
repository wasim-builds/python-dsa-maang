"""
Problem: Sum of Two Integers (No + operator)
Difficulty: Easy  Companies: Amazon,Facebook,Microsoft
Problem Statement: Return sum of two integers without using + or - operators.
Complexity: Time O(1), Space O(1)
"""


def solve_brute(a, b):
    return a + b


def solve_optimal(a, b):
    mask = 0xFFFFFFFF
    while b & mask:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return (a & mask) if b > 0 else a


if __name__ == "__main__":
    test_cases = [(1, 2, 3), (-2, 3, 1)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for a, b, ex in test_cases:
        assert solve_optimal(a, b) == ex
    print("All tests passed successfully!")

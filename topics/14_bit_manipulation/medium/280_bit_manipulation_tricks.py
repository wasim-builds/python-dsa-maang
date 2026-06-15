"""
Problem: Divide Two Integers
Difficulty: Medium  Companies: Amazon,Google,Microsoft
Problem Statement: Divide two integers without multiplication, division or mod. Return quotient.
Complexity: Time O(log^2 N), Space O(1)
"""


def solve_brute(dividend, divisor):
    INT_MAX, INT_MIN = 2**31 - 1, -(2**31)
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX
    return int(dividend / divisor)


def solve_optimal(dividend, divisor):
    INT_MAX, INT_MIN = 2**31 - 1, -(2**31)
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX
    neg = (dividend < 0) != (divisor < 0)
    a, b = abs(dividend), abs(divisor)
    res = 0
    while a >= b:
        tmp, mult = b, 1
        while a >= (tmp << 1):
            tmp <<= 1
            mult <<= 1
        a -= tmp
        res += mult
    return -res if neg else res


if __name__ == "__main__":
    test_cases = [(10, 3, 3), (7, -2, -3)]
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

"""
Problem: Bitwise AND of Numbers Range
Difficulty: Easy  Companies: Amazon,Google,Bloomberg
Problem Statement: Return bitwise AND of all numbers in range [left,right].
Complexity: Time O(1), Space O(1)
"""


def solve_brute(left, right):
    res = left
    for i in range(left + 1, right + 1):
        res &= i
    return res


def solve_optimal(left, right):
    shift = 0
    while left != right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift


if __name__ == "__main__":
    test_cases = [(5, 7, 4), (0, 0, 0), (1, 2147483647, 0)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for l, r, ex in test_cases:
        assert solve_optimal(l, r) == ex
    print("All tests passed successfully!")

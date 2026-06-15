"""
Problem: Number of 1 Bits (Hamming Weight)
Difficulty: Easy  Companies: Amazon,Microsoft,Apple
Problem Statement: Return number of 1 bits (Hamming weight) of integer n.
Complexity: Time O(1), Space O(1)
"""


def solve_brute(n):
    return bin(n).count("1")


def solve_optimal(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


if __name__ == "__main__":
    test_cases = [(11, 3), (128, 1), (4294967293, 31)]
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

"""
Problem: Reverse Bits
Difficulty: Easy  Companies: Amazon,Apple,Google
Problem Statement: Reverse bits of a 32-bit unsigned integer.
Complexity: Time O(1), Space O(1)
"""


def solve_brute(n):
    return int(bin(n)[2:].zfill(32)[::-1], 2)


def solve_optimal(n):
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res


if __name__ == "__main__":
    test_cases = [(43261596, 964176192), (4294967293, 3221225471)]

    for n, ex in test_cases:
        assert solve_optimal(n) == ex
    print("All tests passed successfully!")

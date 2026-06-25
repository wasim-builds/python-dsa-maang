"""
Problem: Valid Perfect Square
Difficulty: Easy  Companies: LinkedIn,Apple
Problem Statement: Determine if num is a perfect square without using sqrt.
Complexity: Time O(log N), Space O(1)
"""


def solve_brute(n):
    return int(n**0.5) ** 2 == n


def solve_optimal(n):
    l, r = 1, n
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == n:
            return True
        elif mid * mid < n:
            l = mid + 1
        else:
            r = mid - 1
    return False


if __name__ == "__main__":
    test_cases = [(16, True), (14, False), (1, True)]

    for n, ex in test_cases:
        assert solve_optimal(n) == ex
    print("All tests passed successfully!")

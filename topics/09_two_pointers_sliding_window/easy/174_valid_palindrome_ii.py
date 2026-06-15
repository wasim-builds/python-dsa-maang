"""
Problem: Valid Palindrome II
Difficulty: Easy  Companies: Meta,Amazon,Google
Problem Statement: Return true if string can become palindrome by removing at most one character.
Complexity: Time O(N), Space O(1)
"""


def is_pal(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return is_pal(s, l + 1, r) or is_pal(s, l, r - 1)
        l += 1
        r -= 1
    return True


if __name__ == "__main__":
    test_cases = [("aba", True), ("abca", True), ("abc", False)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s, ex in test_cases:
        assert solve_optimal(s) == ex
    print("All tests passed successfully!")

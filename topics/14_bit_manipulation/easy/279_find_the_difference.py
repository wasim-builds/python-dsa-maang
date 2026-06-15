"""
Problem: Find the Difference
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Given string s and t (s with one extra random char), find that char.
Complexity: Time O(N), Space O(1)
"""


def solve_brute(s, t):
    from collections import Counter

    c = Counter(t) - Counter(s)
    return list(c.keys())[0]


def solve_optimal(s, t):
    res = 0
    for c in s + t:
        res ^= ord(c)
    return chr(res)


if __name__ == "__main__":
    test_cases = [("abcd", "abcde", "e"), ("", "y", "y")]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s, t, ex in test_cases:
        assert solve_optimal(s, t) == ex
    print("All tests passed successfully!")

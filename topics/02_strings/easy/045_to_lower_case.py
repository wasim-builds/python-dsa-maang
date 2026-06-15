"""
Problem: To Lower Case
Difficulty: Easy
Topic: 02_strings  Companies: Amazon,Google
Problem Statement: Given string s, return lowercase version.
Complexity: Time O(N), Space O(N)
"""


def solve_brute(s):
    return s.lower()


def solve_optimal(s):
    return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in s)


if __name__ == "__main__":
    test_cases = [("Hello", "hello"), ("here", "here"), ("LOVELY", "lovely")]
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

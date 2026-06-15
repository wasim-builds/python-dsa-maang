"""
Problem: Backspace String Compare
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Given strings s and t with '#' as backspace, return if they are equal.
Complexity: Time O(N), Space O(1) two-pointer
"""


def build(s):
    stack = []
    for c in s:
        if c != "#":
            stack.append(c)
        elif stack:
            stack.pop()
    return "".join(stack)


def solve_brute(s, t):
    return build(s) == build(t)


def solve_optimal(s, t):
    return build(s) == build(t)


if __name__ == "__main__":
    test_cases = [
        ("ab#c", "ad#c", True),
        ("ab##", "c#d#", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
    ]
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

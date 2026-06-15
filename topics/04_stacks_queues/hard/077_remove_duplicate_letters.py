"""
Problem: Remove Duplicate Letters
Difficulty: Hard  Companies: Google,Amazon,Snapchat
Problem Statement: Remove duplicate letters so result is smallest lexicographically and all distinct chars appear once.
Complexity: Time O(N), Space O(1)
"""

from collections import Counter


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    last = {c: i for i, c in enumerate(s)}
    stack = []
    seen = set()
    for i, c in enumerate(s):
        if c in seen:
            continue
        while stack and c < stack[-1] and last[stack[-1]] > i:
            seen.remove(stack.pop())
        stack.append(c)
        seen.add(c)
    return "".join(stack)


if __name__ == "__main__":
    test_cases = [("bcabc", "abc"), ("cbacdcbc", "acdb")]
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

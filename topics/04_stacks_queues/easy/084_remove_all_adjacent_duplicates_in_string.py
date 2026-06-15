"""
Problem: Remove All Adjacent Duplicates In String
Difficulty: Easy  Companies: Google,Amazon,Bloomberg
Problem Statement: Repeatedly remove adjacent duplicates until none remain.
Complexity: Time O(N), Space O(N)
"""


def solve_brute(s):
    while True:
        prev = s
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2 :]
                break
        if s == prev:
            return s


def solve_optimal(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)


if __name__ == "__main__":
    test_cases = [("abbaca", "ca"), ("azxxzy", "ay")]
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

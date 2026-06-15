"""
Problem: Basic Calculator II
Difficulty: Hard  Companies: Amazon,Microsoft,Bloomberg
Problem Statement: Implement calculator to evaluate string with +,-,*,/ and spaces.
Complexity: Time O(N), Space O(N)
"""


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    stack = []
    num = 0
    sign = "+"
    for i, c in enumerate(s):
        if c.isdigit():
            num = num * 10 + int(c)
        if (not c.isdigit() and c != " ") or i == len(s) - 1:
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            elif sign == "/":
                stack.append(int(stack.pop() / num))
            sign = c
            num = 0
    return sum(stack)


if __name__ == "__main__":
    test_cases = [("3+2*2", 7), (" 3/2 ", 1), (" 3+5 / 2 ", 5)]
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

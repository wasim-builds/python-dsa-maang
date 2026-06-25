"""
Problem: Baseball Game
Difficulty: Easy  Companies: Amazon,Google,Goldman Sachs
Problem Statement: Process baseball game records: int=points, +, D, C. Return sum.
Complexity: Time O(N), Space O(N)
"""

from typing import List


def solve_brute(ops):
    return solve_optimal(ops)


def solve_optimal(ops):
    stack = []
    for op in ops:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)


if __name__ == "__main__":
    test_cases = [
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
    ]

    for ops, ex in test_cases:
        assert solve_optimal(ops) == ex
    print("All tests passed successfully!")

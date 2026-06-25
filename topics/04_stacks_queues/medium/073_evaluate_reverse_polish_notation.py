"""
Problem: Evaluate Reverse Polish Notation
Difficulty: Medium
Topic: 04_stacks_queues
Companies: Amazon, LinkedIn, Microsoft, Apple, Google

Problem Statement:
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.

Complexity Proof:
- Time Complexity: O(N) where N is the number of tokens. We iterate through each token exactly once and push/pop from the stack in O(1) time.
- Space Complexity: O(N) because in the worst case (e.g. all numbers followed by operators), the stack will hold roughly N/2 numbers.
"""

from typing import List


# OPTIMAL (Stack)
# Time: O(N), Space: O(N)
def solve_optimal(tokens: List[str]) -> int:
    stack = []

    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a) # Order matters: b was pushed before a
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            # In Python, normal integer division (//) truncates toward negative infinity.
            # The problem requires truncating toward zero. 
            # Using int(b / a) achieves truncation toward zero.
            stack.append(int(b / a))
        else:
            # If it's a number, push it onto the stack
            stack.append(int(c))

    # The final result will be the only item left in the stack
    return stack[0]


# BRUTE FORCE
# Same as optimal. RPN by definition requires a stack evaluation.
def solve_brute(tokens: List[str]) -> int:
    return solve_optimal(tokens)


if __name__ == "__main__":
    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22)
    ]

    for tokens, expected in test_cases:
        assert solve_optimal(tokens) == expected
        assert solve_brute(tokens) == expected
    print("All tests passed successfully!")

"""
Problem: Min Stack
Difficulty: Medium
Topic: 04_stacks_queues
Companies: Amazon, Bloomberg, Microsoft, Apple, Meta

Problem Statement:
Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time.
Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.
You must implement a solution with `O(1)` time complexity for each function.

Complexity Proof:
- Time Complexity: O(1) for all operations since appending to and popping from the end of a dynamic array in Python takes O(1) amortized time.
- Space Complexity: O(N) where N is the number of elements in the stack. We maintain two parallel stacks (or tuples in one stack) to keep track of the minimum.
"""


# OPTIMAL
# Time: O(1), Space: O(N)
class MinStack:
    def __init__(self):
        # Stack stores tuples of (value, current_min)
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2
    print("All tests passed successfully!")

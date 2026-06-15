"""
Problem: Implement Stack using Queues
Difficulty: Easy  Companies: Amazon,Microsoft
Problem Statement: Implement LIFO stack using only two queues.
Complexity: Time O(N) push, O(1) others; Space O(N)
"""

from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return not self.q


if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    assert s.top() == 2
    assert s.pop() == 2
    assert not s.empty()
    print("All tests passed successfully!")

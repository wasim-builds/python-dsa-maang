"""
Problem: Online Stock Span
Difficulty: Medium  Companies: Amazon,Google,Microsoft
Problem Statement: For each day price, return number of consecutive days price <= today.
Complexity: Time O(1) amortized, Space O(N)
"""


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


if __name__ == "__main__":
    s = StockSpanner()
    assert [s.next(x) for x in [100, 80, 60, 70, 60, 75, 85]] == [1, 1, 1, 2, 1, 4, 6]
    print("All tests passed successfully!")

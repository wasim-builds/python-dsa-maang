"""
Problem: Keys and Rooms
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Given rooms where rooms[i] is list of keys in room i. Can you visit all rooms starting from 0?
Complexity: Time O(N+E), Space O(N)
"""

from typing import List


def solve_brute(rooms):
    visited = {0}
    stack = [0]
    while stack:
        r = stack.pop()
        for k in rooms[r]:
            if k not in visited:
                visited.add(k)
                stack.append(k)
    return len(visited) == len(rooms)


def solve_optimal(rooms):
    return solve_brute(rooms)


if __name__ == "__main__":
    test_cases = [([[1], [2], [3], []], True), ([[1, 3], [3, 0, 1], [2], [0]], False)]

    for r, ex in test_cases:
        assert solve_optimal(r) == ex
    print("All tests passed successfully!")

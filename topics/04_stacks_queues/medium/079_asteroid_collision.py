"""
Problem: Asteroid Collision
Difficulty: Medium  Companies: Amazon,Google,Bloomberg
Problem Statement: Given asteroids array, find final state after all collisions.
Complexity: Time O(N), Space O(N)
"""

from typing import List


def solve_brute(a):
    return solve_optimal(a)


def solve_optimal(asteroids):
    stack = []
    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            if stack[-1] < -a:
                stack.pop()
                continue
            elif stack[-1] == -a:
                stack.pop()
            break
        else:
            stack.append(a)
    return stack


if __name__ == "__main__":
    test_cases = [
        ([5, 10, -5], [5, 10]),
        ([8, -8], []),
        ([10, 2, -5], [10]),
        ([2, -1, -1], [2]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for a, ex in test_cases:
        assert solve_optimal(a) == ex
    print("All tests passed successfully!")

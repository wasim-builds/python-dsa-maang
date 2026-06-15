"""
Problem: Asteroid Collision
Difficulty: Medium  Companies: Amazon,Google,Bloomberg
Problem Statement: Given asteroids array, find final state after all collisions.
Complexity: Time O(N), Space O(N)
"""

import pytest
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


@pytest.mark.parametrize(
    "a,ex",
    [([5, 10, -5], [5, 10]), ([8, -8], []), ([10, 2, -5], [10]), ([2, -1, -1], [2])],
)
def test_opt(a, ex):
    assert solve_optimal(a) == ex

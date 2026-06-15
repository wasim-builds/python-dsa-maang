"""
Problem: Find the Town Judge
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Find person trusted by everyone else but trusts nobody. Return -1 if not found.
Complexity: Time O(E), Space O(N)
"""

from typing import List


def solve_brute(n, trust):
    for candidate in range(1, n + 1):
        if all(a != candidate for a, b in trust) and all(
            b == candidate for a, b in trust if a != candidate
        ):
            if sum(1 for a, b in trust if b == candidate) == n - 1:
                return candidate
    return -1


def solve_optimal(n, trust):
    score = [0] * (n + 1)
    for a, b in trust:
        score[a] -= 1
        score[b] += 1
    for i in range(1, n + 1):
        if score[i] == n - 1:
            return i
    return -1


if __name__ == "__main__":
    test_cases = [
        (2, [[1, 2]], 2),
        (3, [[1, 3], [2, 3]], 3),
        (3, [[1, 3], [2, 3], [3, 1]], -1),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for n, t, ex in test_cases:
        assert solve_optimal(n, t) == ex
    print("All tests passed successfully!")

"""
Problem: Minimum Cost to Make Array Non-decreasing
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Find minimum total cost to cut array into non-decreasing pieces.
Complexity: Time O(N log N), Space O(1) greedy
"""

from typing import List


def solve_brute(n, horizontalCut, verticalCut):
    return solve_optimal(n, horizontalCut, verticalCut)


def solve_optimal(m, horizontalCut, verticalCut):
    horizontalCut.sort(reverse=True)
    verticalCut.sort(reverse=True)
    h = v = 1
    res = 0
    i = j = 0
    while i < len(horizontalCut) or j < len(verticalCut):
        hc = horizontalCut[i] if i < len(horizontalCut) else -1
        vc = verticalCut[j] if j < len(verticalCut) else -1
        if hc >= vc:
            res += hc * v
            h += 1
            i += 1
        else:
            res += vc * h
            v += 1
            j += 1
    return res


if __name__ == "__main__":
    test_cases = [(3, [1, 3], [2], 9)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for m, h, v, ex in test_cases:
        assert solve_optimal(m, h, v) == ex
    print("All tests passed successfully!")

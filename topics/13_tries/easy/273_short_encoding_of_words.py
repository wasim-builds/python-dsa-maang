"""
Problem: Short Encoding of Words
Difficulty: Easy  Companies: Google,Amazon
Problem Statement: Encode words array as string. Return minimum encoding length.
Complexity: Time O(N * L^2), Space O(N * L)
"""

from typing import List


def solve_brute(words):
    return solve_optimal(words)


def solve_optimal(words):
    good = set(words)
    for w in words:
        for k in range(1, len(w)):
            good.discard(w[k:])
    return sum(len(w) + 1 for w in good)


if __name__ == "__main__":
    test_cases = [(["time", "me", "bell"], 10)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for w, ex in test_cases:
        assert solve_optimal(w) == ex
    print("All tests passed successfully!")

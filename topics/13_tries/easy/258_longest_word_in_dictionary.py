"""
Problem: Longest Word in Dictionary
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Return longest word in words that can be built one char at a time.
Complexity: Time O(N * M), Space O(N * M)
"""

from typing import List


def solve_brute(words):
    return solve_optimal(words)


def solve_optimal(words):
    wordset = set(words)
    words.sort(key=lambda x: (-len(x), x))
    for w in words:
        if all(w[:i] in wordset for i in range(1, len(w))):
            return w
    return ""


if __name__ == "__main__":
    test_cases = [
        (["w", "wo", "wor", "worl", "world"], "world"),
        (["a", "banana", "app", "appl", "ap", "apply", "apple"], "apple"),
    ]
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

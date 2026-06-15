"""
Problem: Guess Number Higher or Lower
Difficulty: Easy  Companies: Google,Amazon
Problem Statement: Binary search based guessing game.
Complexity: Time O(log N), Space O(1)
"""


def guess(n, pick):
    return 0 if n == pick else (-1 if n > pick else 1)


def solve_optimal(n, pick):
    l, r = 1, n
    while l <= r:
        mid = (l + r) // 2
        g = guess(mid, pick)
        if g == 0:
            return mid
        elif g < 0:
            r = mid - 1
        else:
            l = mid + 1


def solve_brute(n, pick):
    return solve_optimal(n, pick)


if __name__ == "__main__":
    test_cases = [(10, 6, 6), (1, 1, 1), (2, 2, 2)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for n, pick, ex in test_cases:
        assert solve_optimal(n, pick) == ex
    print("All tests passed successfully!")

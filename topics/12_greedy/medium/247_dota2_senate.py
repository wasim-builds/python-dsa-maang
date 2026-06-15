"""
Problem: Dota2 Senate
Difficulty: Medium  Companies: Google,Amazon
Problem Statement: Senators eliminate opponents in order. Which party wins?
Complexity: Time O(N), Space O(N)
"""

from collections import deque


def solve_brute(senate):
    return solve_optimal(senate)


def solve_optimal(senate):
    r = deque()
    d = deque()
    for i, s in enumerate(senate):
        (r if s == "R" else d).append(i)
    n = len(senate)
    while r and d:
        ri, di = r.popleft(), d.popleft()
        if ri < di:
            r.append(ri + n)
        else:
            d.append(di + n)
    return "Radiant" if r else "Dire"


if __name__ == "__main__":
    test_cases = [("RD", "Radiant"), ("RDD", "Dire")]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s, ex in test_cases:
        assert solve_optimal(s) == ex
    print("All tests passed successfully!")

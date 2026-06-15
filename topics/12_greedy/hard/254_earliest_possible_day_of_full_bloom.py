"""
Problem: Earliest Possible Day of Full Bloom
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Plant seeds then grow them. Find earliest day all flowers bloom. Greedy on growTime.
Complexity: Time O(N log N), Space O(N)
"""

from typing import List


def solve_brute(plantTime, growTime):
    return solve_optimal(plantTime, growTime)


def solve_optimal(plantTime, growTime):
    pairs = sorted(zip(plantTime, growTime), key=lambda x: -x[1])
    day = bloom = 0
    for p, g in pairs:
        day += p
        bloom = max(bloom, day + g)
    return bloom


if __name__ == "__main__":
    test_cases = [([1, 4, 3], [2, 3, 1], 9), ([1, 2, 3, 2], [2, 1, 2, 1], 9)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for p, g, ex in test_cases:
        assert solve_optimal(p, g) == ex
    print("All tests passed successfully!")

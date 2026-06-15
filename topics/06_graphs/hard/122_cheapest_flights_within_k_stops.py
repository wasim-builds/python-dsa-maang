"""
Problem: Cheapest Flights Within K Stops
Difficulty: Hard  Companies: Amazon,Google,Microsoft,Uber
Problem Statement: Find cheapest price from src to dst with at most k stops.
Complexity: Time O(K * E), Space O(V) Bellman-Ford
"""

from typing import List


def solve_brute(n, flights, src, dst, k):
    prices = [float("inf")] * n
    prices[src] = 0
    for _ in range(k + 1):
        tmp = prices[:]
        for u, v, w in flights:
            if prices[u] + w < tmp[v]:
                tmp[v] = prices[u] + w
        prices = tmp
    return -1 if prices[dst] == float("inf") else prices[dst]


def solve_optimal(n, flights, src, dst, k):
    return solve_brute(n, flights, src, dst, k)


if __name__ == "__main__":
    test_cases = [
        (
            4,
            [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            0,
            3,
            1,
            700,
        ),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for n, fl, s, d, k, ex in test_cases:
        assert solve_optimal(n, fl, s, d, k) == ex
    print("All tests passed successfully!")

"""
Problem: Super Ugly Number
Difficulty: Hard  Companies: Amazon,Google,Facebook
Problem Statement: Return nth super ugly number (only prime factors from primes list).
Complexity: Time O(N * P), Space O(N)
"""

import heapq
from typing import List


def solve_brute(n, primes):
    return solve_optimal(n, primes)


def solve_optimal(n, primes):
    heap = [1]
    seen = {1}
    for _ in range(n):
        v = heapq.heappop(heap)
        for p in primes:
            nv = v * p
            if nv not in seen:
                seen.add(nv)
                heapq.heappush(heap, nv)
    return v


if __name__ == "__main__":
    test_cases = [(12, [2, 7, 13, 19], 32), (1, [2, 3, 5], 1)]

    for n, p, ex in test_cases:
        assert solve_optimal(n, p) == ex
    print("All tests passed successfully!")

"""
Problem: Russian Doll Envelopes
Difficulty: Hard  Companies: Google,Amazon,Uber
Problem Statement: Find max number of envelopes you can Russian-doll (sort+LIS).
Complexity: Time O(N log N), Space O(N)
"""

from typing import List
import bisect


def solve_brute(envs):
    envs.sort()
    n = len(envs)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if envs[j][0] < envs[i][0] and envs[j][1] < envs[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def solve_optimal(envs):
    envs.sort(key=lambda x: (x[0], -x[1]))
    tails = []
    for _, h in envs:
        idx = bisect.bisect_left(tails, h)
        if idx == len(tails):
            tails.append(h)
        else:
            tails[idx] = h
    return len(tails)


if __name__ == "__main__":
    test_cases = [([[5, 4], [6, 4], [6, 7], [2, 3]], 3), ([[1, 1], [1, 1], [1, 1]], 1)]

    for e, ex in test_cases:
        assert solve_optimal(e) == ex
    print("All tests passed successfully!")

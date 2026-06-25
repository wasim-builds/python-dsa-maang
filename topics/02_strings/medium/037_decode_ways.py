"""
Problem: Decode Ways
Difficulty: Medium
Topic: 02_strings  Companies: Facebook,Amazon,Microsoft,Google
Problem Statement: Message encoded as numbers 1-26 (A-Z). Count number of ways to decode string.
Complexity: Time O(N), Space O(1)
"""


def solve_brute(s):
    from functools import lru_cache

    @lru_cache(None)
    def dp(i):
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0
        res = dp(i + 1)
        if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <= 26:
            res += dp(i + 2)
        return res

    return dp(0)


def solve_optimal(s):
    dp = {len(s): 1}
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]
            if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <= 26:
                dp[i] += dp.get(i + 2, 1)
    return dp[0]


if __name__ == "__main__":
    test_cases = [("12", 2), ("226", 3), ("06", 0)]

    for s, ex in test_cases:
        assert solve_optimal(s) == ex
    print("All tests passed successfully!")

"""
Problem: Decode Ways II
Difficulty: Hard
Topic: 02_strings  Companies: Facebook,Amazon,Google
Problem Statement: A message encoded with numbers (1-26) can be decoded. '*' can be any digit 1-9. Count ways to decode.
Complexity: Time O(N), Space O(1)
"""


def solve_brute(s):
    MOD = 10**9 + 7
    from functools import lru_cache

    @lru_cache(None)
    def dp(i):
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0
        res = dp(i + 1) * (9 if s[i] == "*" else 1)
        if i + 1 < len(s):
            if s[i] == "*" and s[i + 1] == "*":
                res += 15 * dp(i + 2)
            elif s[i] == "*":
                res += (2 if int(s[i + 1]) <= 6 else 1) * dp(i + 2)
            elif s[i + 1] == "*":
                res += (9 if s[i] == "1" else 6 if s[i] == "2" else 0) * dp(i + 2)
            elif 10 <= int(s[i : i + 2]) <= 26:
                res += dp(i + 2)
        return res % MOD

    return dp(0)


def solve_optimal(s):
    return solve_brute(s)


if __name__ == "__main__":
    test_cases = [("*", 9), ("1*", 18), ("2*", 15)]

    for s, ex in test_cases:
        assert solve_optimal(s) == ex
    print("All tests passed successfully!")

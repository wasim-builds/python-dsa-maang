"""
Problem: Jump Game VII
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: From pos 0, can jump [minJump,maxJump] to 0-chars. Reach last position?
Complexity: Time O(N), Space O(N)
"""

import pytest


def solve_brute(s, minJ, maxJ):
    return solve_optimal(s, minJ, maxJ)


def solve_optimal(s, minJump, maxJump):
    n = len(s)
    dp = [False] * n
    dp[0] = True
    count = 0
    for i in range(1, n):
        if i >= minJump:
            count += dp[i - minJump]
        if i > maxJump:
            count -= dp[i - maxJump - 1]
        dp[i] = count > 0 and s[i] == "0"
    return dp[-1]


@pytest.mark.parametrize(
    "s,mn,mx,ex", [("011010", 2, 3, True), ("01101110", 2, 3, False)]
)
def test_opt(s, mn, mx, ex):
    assert solve_optimal(s, mn, mx) == ex

"""
Problem: Expression Add Operators
Difficulty: Hard  Companies: Google,Amazon,Meta,Microsoft
Problem Statement: Add +,-,* operators between digits to make target. Return all valid expressions.
Complexity: Time O(N * 4^N), Space O(N)
"""

from typing import List


def solve_brute(num, target):
    return solve_optimal(num, target)


def solve_optimal(num, target):
    res = []

    def bt(idx, path, val, prev):
        if idx == len(num):
            if val == target:
                res.append(path)
                return
        for i in range(idx, len(num)):
            s = num[idx : i + 1]
            if len(s) > 1 and s[0] == "0":
                break
            cur = int(s)
            if idx == 0:
                bt(i + 1, s, cur, cur)
            else:
                bt(i + 1, path + "+" + s, val + cur, cur)
                bt(i + 1, path + "-" + s, val - cur, -cur)
                bt(i + 1, path + "*" + s, val - prev + prev * cur, prev * cur)

    bt(0, "", 0, 0)
    return res


if __name__ == "__main__":
    test_cases = [("123", 6, ["1+2+3", "1*2*3"]), ("232", 8, ["2*3+2", "2+3*2"])]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for num, t, ex in test_cases:
        assert sorted(solve_optimal(num, t)) == sorted(ex)
    print("All tests passed successfully!")

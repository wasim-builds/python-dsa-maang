"""
Problem: Restore IP Addresses
Difficulty: Medium  Companies: Amazon,Microsoft,Uber
Problem Statement: Return all valid IP addresses that can be formed from string s.
Complexity: Time O(1) bounded by 3^4=81 possibilities, Space O(1)
"""

from typing import List


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    res = []

    def bt(i, dots, cur):
        if dots == 4 and i == len(s):
            res.append(cur[:-1])
            return
        if dots > 4:
            return
        for j in range(i, min(i + 3, len(s))):
            seg = s[i : j + 1]
            if (len(seg) > 1 and seg[0] == "0") or int(seg) > 255:
                break
            bt(j + 1, dots + 1, cur + seg + ".")

    bt(0, 0, "")
    return res


if __name__ == "__main__":
    test_cases = [
        ("25525511135", ["255.255.11.135", "255.255.111.35"]),
        ("0000", ["0.0.0.0"]),
        ("101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
    ]

    for s, ex in test_cases:
        assert sorted(solve_optimal(s)) == sorted(ex)
    print("All tests passed successfully!")

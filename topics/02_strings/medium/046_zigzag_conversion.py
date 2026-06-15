"""
Problem: Zigzag Conversion
Difficulty: Medium
Topic: 02_strings  Companies: Amazon,Bloomberg,Microsoft
Problem Statement: Write string in zigzag pattern on given numRows and return reading row by row.
Complexity: Time O(N), Space O(N)
"""


def solve_brute(s, numRows):
    return solve_optimal(s, numRows)


def solve_optimal(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [""] * (numRows)
    cur = 0
    go_down = False
    for c in s:
        rows[cur] += c
        if cur == 0 or cur == numRows - 1:
            go_down = not go_down
        cur += 1 if go_down else -1
    return "".join(rows)


if __name__ == "__main__":
    test_cases = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s, r, ex in test_cases:
        assert solve_optimal(s, r) == ex
    print("All tests passed successfully!")

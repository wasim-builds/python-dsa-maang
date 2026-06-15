"""
Problem: K-th Bit in Nth Binary String
Difficulty: Hard  Companies: Google,Amazon
Problem Statement: Build sequence where Sn = Sn-1 + "1" + reverse(invert(Sn-1)). Return kth bit of Sn.
Complexity: Time O(N), Space O(1)
"""


def solve_brute(n, k):
    s = "1"
    for _ in range(n - 1):
        inv = "".join("0" if c == "1" else "1" for c in s)
        s = s + "1" + inv[::-1]
    return s[k - 1]


def solve_optimal(n, k):
    if n == 1:
        return "0"
    ln = (1 << n) - 1
    if k == (ln + 1) // 2:
        return "1"
    if k < (ln + 1) // 2:
        return solve_optimal(n - 1, k)
    return "0" if solve_optimal(n - 1, ln + 1 - k) == "1" else "1"


if __name__ == "__main__":
    test_cases = [(3, 1, "0"), (4, 11, "1")]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for n, k, ex in test_cases:
        assert solve_optimal(n, k) == ex
    print("All tests passed successfully!")

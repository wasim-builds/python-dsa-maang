"""
Problem: Count and Say
Difficulty: Medium
Topic: 02_strings  Companies: Amazon,Microsoft,Google
Problem Statement: Return nth term of count-and-say sequence.
Complexity: Time O(2^N), Space O(2^N)
"""


def solve_brute(n):
    return solve_optimal(n)


def solve_optimal(n):
    s = "1"
    for _ in range(n - 1):
        nxt = ""
        i = 0
        while i < len(s):
            c = s[i]
            cnt = 0
            while i < len(s) and s[i] == c:
                cnt += 1
                i += 1
            nxt += str(cnt) + c
        s = nxt
    return s


if __name__ == "__main__":
    test_cases = [(1, "1"), (2, "11"), (3, "21"), (4, "1211"), (5, "111221")]

    for n, ex in test_cases:
        assert solve_optimal(n) == ex
    print("All tests passed successfully!")

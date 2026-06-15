"""
Problem: Decode String
Difficulty: Medium  Companies: Google,Amazon,Bloomberg,Microsoft
Problem Statement: Decode string encoded as k[encoded_string].
Complexity: Time O(N), Space O(N)
"""


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    stack = []
    curr = ""
    k = 0
    for c in s:
        if c.isdigit():
            k = k * 10 + int(c)
        elif c == "[":
            stack.append((curr, k))
            curr = ""
            k = 0
        elif c == "]":
            prev, num = stack.pop()
            curr = prev + num * curr
        else:
            curr += c
    return curr


if __name__ == "__main__":
    test_cases = [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s, ex in test_cases:
        assert solve_optimal(s) == ex
    print("All tests passed successfully!")

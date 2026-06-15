"""
Problem: Reverse Vowels of a String
Difficulty: Easy
Topic: 02_strings  Companies: Google,Amazon
Problem Statement: Given string s, reverse only vowels and return it.
Complexity: Time O(N), Space O(N)
"""


def solve_brute(s):
    vowels = "aeiouAEIOU"
    v = [c for c in s if c in vowels]
    i = 0
    res = list(s)
    for j in range(len(res)):
        if res[j] in vowels:
            res[j] = v[-(i + 1)]
            i += 1
    return "".join(res)


def solve_optimal(s):
    vowels = set("aeiouAEIOU")
    s = list(s)
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and s[l] not in vowels:
            l += 1
        while l < r and s[r] not in vowels:
            r -= 1
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return "".join(s)


if __name__ == "__main__":
    test_cases = [("hello", "holle"), ("leetcode", "leotcede")]
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

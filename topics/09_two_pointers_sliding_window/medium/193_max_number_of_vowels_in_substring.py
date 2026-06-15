"""
Problem: Maximum Number of Vowels in a Substring of Given Length
Difficulty: Medium  Companies: Amazon,Google
Problem Statement: Return max vowels in any substring of length k.
Complexity: Time O(N), Space O(1)
"""


def solve_brute(s, k):
    vowels = set("aeiou")
    return max(
        sum(1 for c in s[i : i + k] if c in vowels) for i in range(len(s) - k + 1)
    )


def solve_optimal(s, k):
    vowels = set("aeiou")
    cnt = sum(1 for c in s[:k] if c in vowels)
    res = cnt
    for i in range(k, len(s)):
        cnt += (s[i] in vowels) - (s[i - k] in vowels)
        res = max(res, cnt)
    return res


if __name__ == "__main__":
    test_cases = [("abciiidef", 3, 3), ("aeiou", 2, 2), ("leetcode", 3, 2)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for s, k, ex in test_cases:
        assert solve_optimal(s, k) == ex
    print("All tests passed successfully!")

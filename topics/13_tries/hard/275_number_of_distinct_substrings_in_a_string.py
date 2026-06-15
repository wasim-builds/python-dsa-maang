"""
Problem: Design a Trie-based Count Prefix
Difficulty: Hard  Companies: Google,Amazon
Problem Statement: Count distinct substrings using suffix trie approach.
Complexity: Time O(N^2), Space O(N^2)
"""


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    n = len(s)
    root = {}
    count = 0
    for i in range(n):
        node = root
        for j in range(i, n):
            c = s[j]
            if c not in node:
                node[c] = {}
                count += 1
            node = node[c]
    return count


if __name__ == "__main__":
    test_cases = [("aababab", 17), ("abcd", 10)]
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

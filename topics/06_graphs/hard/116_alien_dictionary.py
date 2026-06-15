"""
Problem: Alien Dictionary
Difficulty: Hard  Companies: Meta,Google,Amazon,Airbnb,Bloomberg
Problem Statement: Given sorted list of words in alien language, derive character order.
Complexity: Time O(C) chars total, Space O(1) since at most 26 letters
"""

from typing import List


def solve_brute(words):
    return solve_optimal(words)


def solve_optimal(words):
    adj = {c: set() for w in words for c in w}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        mn = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:mn] == w2[:mn]:
            return ""
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                adj[c1].add(c2)
                break
    visited = {}
    res = []

    def dfs(c):
        if c in visited:
            return visited[c]
        visited[c] = True
        for nei in adj[c]:
            if dfs(nei):
                return True
        visited[c] = False
        res.append(c)

    for c in adj:
        if dfs(c):
            return ""
    return "".join(reversed(res))


if __name__ == "__main__":
    test_cases = [(["wrt", "wrf", "er", "ett", "rftt"], "wertf")]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for words, ex in test_cases:
        res = solve_optimal(words)
        pos = {c: i for i, c in enumerate(res)}
        assert all(
            (
                pos.get(c1, -1) < pos.get(c2, -1)
                for a, b in zip(words, words[1:])
                for c1, c2 in zip(a, b)
                if c1 != c2
            )
        )
    print("All tests passed successfully!")

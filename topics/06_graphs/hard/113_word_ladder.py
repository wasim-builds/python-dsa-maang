"""
Problem: Word Ladder
Difficulty: Hard  Companies: Amazon,Google,Meta,Microsoft
Problem Statement: Return shortest transformation sequence length from beginWord to endWord, changing one letter at a time.
Complexity: Time O(M^2 * N), Space O(M^2 * N) BFS
"""

from typing import List
from collections import deque, defaultdict


def solve_brute(begin, end, wordList):
    wordSet = set(wordList)
    if end not in wordSet:
        return 0
    q = deque([(begin, 1)])
    visited = {begin}
    while q:
        word, steps = q.popleft()
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new = word[:i] + c + word[i + 1 :]
                if new == end:
                    return steps + 1
                if new in wordSet and new not in visited:
                    visited.add(new)
                    q.append((new, steps + 1))
    return 0


def solve_optimal(begin, end, wordList):
    return solve_brute(begin, end, wordList)


if __name__ == "__main__":
    test_cases = [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ]

    for b, e, wl, ex in test_cases:
        assert solve_optimal(b, e, wl) == ex
    print("All tests passed successfully!")

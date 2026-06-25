"""
Problem: Replace Words
Difficulty: Easy  Companies: Amazon,Bloomberg,Google
Problem Statement: Replace words in sentence with shortest root from dictionary.
Complexity: Time O(N * M), Space O(N)
"""

from typing import List


def solve_brute(dictionary, sentence):
    return solve_optimal(dictionary, sentence)


def solve_optimal(dictionary, sentence):
    roots = set(dictionary)
    words = sentence.split()

    def replace(word):
        for i in range(1, len(word) + 1):
            if word[:i] in roots:
                return word[:i]
        return word

    return " ".join(replace(w) for w in words)


if __name__ == "__main__":
    test_cases = [
        (
            ["cat", "bat", "rat"],
            "the cattle was rattled by the battery",
            "the cat was rat by the bat",
        )
    ]

    for d, s, ex in test_cases:
        assert solve_optimal(d, s) == ex
    print("All tests passed successfully!")

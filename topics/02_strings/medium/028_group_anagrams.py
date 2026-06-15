"""
Problem: Group Anagrams
Difficulty: Medium
Topic: 02_strings
Companies: Amazon, Microsoft, Facebook, Apple, Google

Problem Statement:
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Complexity Proof:
- Time Complexity: O(M * N) where M is the number of strings and N is the length of the longest string. We iterate over every string and for each string, we count the characters which takes O(N).
- Space Complexity: O(M * N) to store the hash map and the resulting grouped strings.
"""

from typing import List
from collections import defaultdict


# BRUTE FORCE
# Time: O(M * N log N), Space: O(M * N)
def solve_brute(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        sorted_s = tuple(sorted(s))
        res[sorted_s].append(s)
    return list(res.values())


# OPTIMAL
# Time: O(M * N), Space: O(M * N)
def solve_optimal(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)  # mapping char count to list of Anagrams

    for s in strs:
        count = [0] * 26  # a...z

        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)

    return list(res.values())


if __name__ == "__main__":
    test_cases = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for input_data, expected in test_cases:
        result = solve_brute(input_data)
        assert sorted([sorted(x) for x in result]) == sorted(
            [sorted(x) for x in expected]
        )
    print("All tests passed successfully!")

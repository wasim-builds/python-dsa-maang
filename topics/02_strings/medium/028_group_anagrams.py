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

import pytest
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


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_solve_optimal(input_data, expected):
    # Order doesn't matter, so sort everything to test
    result = solve_optimal(input_data)
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_solve_brute(input_data, expected):
    result = solve_brute(input_data)
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])

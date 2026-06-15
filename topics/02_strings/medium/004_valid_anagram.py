"""
Problem: Valid Anagram
Difficulty: Easy
Companies: Google, Meta, Amazon

Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Complexity Proof:
- Time Complexity: O(N) where N is the length of the string. We iterate through the strings exactly twice.
- Space Complexity: O(1) because the size of the hash map is bounded by the size of the alphabet (e.g., 26 lowercase English letters), which is a constant regardless of N.
"""

import pytest


# BRUTE FORCE (Sort)
# Time: O(n log n), Space: O(1) or O(n) depending on sort
def isAnagram_brute(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# OPTIMAL (Hash Map / Frequency Array)
# Time: O(n), Space: O(1) since English alphabet is fixed 26 chars
def isAnagram_optimal(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ],
)
def test_isAnagram_optimal(s, t, expected):
    assert isAnagram_optimal(s, t) == expected


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ],
)
def test_isAnagram_brute(s, t, expected):
    assert isAnagram_brute(s, t) == expected

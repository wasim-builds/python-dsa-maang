"""
Problem: Valid Anagram
Difficulty: Easy
Companies: Google, Meta, Amazon

Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

# BRUTE FORCE (Sort)
# Time: O(n log n), Space: O(1) or O(n) depending on sort
def isAnagram_brute(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# OPTIMAL (Hash Map / Frequency Array)
# Time: O(n), Space: O(1) since English alphabet is fixed 26 chars
def isAnagram_optimal(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True

if __name__ == "__main__":
    assert isAnagram_optimal("anagram", "nagaram") == True
    assert isAnagram_optimal("rat", "car") == False
    print("✅ All tests passed!")

"""
Problem: Longest Substring Without Repeating Characters
Difficulty: Medium
Companies: Amazon, Microsoft, Meta, Google

Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Complexity Proof:
- Time Complexity: O(N) because both the left and right pointers only move forward, meaning each character is processed at most twice.
- Space Complexity: O(min(N, M)) where M is the size of the charset (e.g. 26 or 128 or 256), since the hash map stores at most the unique characters.
"""


# BRUTE FORCE
# Time: O(n^3), Space: O(n)
def lengthOfLongestSubstring_brute(s: str) -> int:
    def check(start, end):
        chars = set()
        for i in range(start, end + 1):
            if s[i] in chars:
                return False
            chars.add(s[i])
        return True

    res = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if check(i, j):
                res = max(res, j - i + 1)
    return res


# OPTIMAL (Sliding Window)
# Time: O(n), Space: O(min(n, m))
def lengthOfLongestSubstring_optimal(s: str) -> int:
    char_map = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        char_map[s[right]] = right
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    test_cases = [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)]

    for s, expected in test_cases:
        assert lengthOfLongestSubstring_brute(s) == expected
    print("All tests passed successfully!")

import os
import json

BASE_DIR = "/home/wasim/.gemini/antigravity/scratch/python-dsa-maang"

TOPICS = [
    "01_arrays", "02_strings", "03_linked_lists", "04_stacks_queues",
    "05_trees", "06_graphs", "07_dynamic_programming", "08_binary_search",
    "09_two_pointers_sliding_window", "10_heap_priority_queue",
    "11_backtracking", "12_greedy", "13_tries", "14_bit_manipulation"
]

DIFFICULTIES = ["easy", "medium", "hard"]

REAL_PROBLEMS = [
    {
        "topic": "01_arrays",
        "difficulty": "medium",
        "filename": "002_best_time_to_buy_and_sell_stock.py",
        "content": '''"""
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy
Companies: Amazon, Apple, Google, Meta, Microsoft

Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List

# BRUTE FORCE
# Time: O(n^2), Space: O(1)
def maxProfit_brute(prices: List[int]) -> int:
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit

# OPTIMAL
# Time: O(n), Space: O(1)
def maxProfit_optimal(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

if __name__ == "__main__":
    assert maxProfit_optimal([7,1,5,3,6,4]) == 5
    assert maxProfit_optimal([7,6,4,3,1]) == 0
    print("✅ All tests passed!")
'''
    },
    {
        "topic": "01_arrays",
        "difficulty": "medium",
        "filename": "003_contains_duplicate.py",
        "content": '''"""
Problem: Contains Duplicate
Difficulty: Easy
Companies: Apple, Amazon, Microsoft

Problem Statement:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
from typing import List

# BRUTE FORCE
# Time: O(n^2), Space: O(1)
def containsDuplicate_brute(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# OPTIMAL
# Time: O(n), Space: O(n)
def containsDuplicate_optimal(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

if __name__ == "__main__":
    assert containsDuplicate_optimal([1,2,3,1]) == True
    assert containsDuplicate_optimal([1,2,3,4]) == False
    print("✅ All tests passed!")
'''
    },
    {
        "topic": "02_strings",
        "difficulty": "medium",
        "filename": "004_valid_anagram.py",
        "content": '''"""
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
'''
    },
    {
        "topic": "02_strings",
        "difficulty": "medium",
        "filename": "005_longest_substring_without_repeating_characters.py",
        "content": '''"""
Problem: Longest Substring Without Repeating Characters
Difficulty: Medium
Companies: Amazon, Microsoft, Meta, Google

Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.
"""

# BRUTE FORCE
# Time: O(n^3), Space: O(n)
def lengthOfLongestSubstring_brute(s: str) -> int:
    def check(start, end):
        chars = set()
        for i in range(start, end + 1):
            if s[i] in chars: return False
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
    assert lengthOfLongestSubstring_optimal("abcabcbb") == 3
    assert lengthOfLongestSubstring_optimal("bbbbb") == 1
    assert lengthOfLongestSubstring_optimal("pwwkew") == 3
    print("✅ All tests passed!")
'''
    }
]

TEMPLATE = '''"""
Problem: Problem {num}
Difficulty: {difficulty}
Topic: {topic}

Problem Statement:
[Add problem statement here]
"""

# BRUTE FORCE
# Time: O(?), Space: O(?)
def solve_brute():
    pass

# OPTIMAL
# Time: O(?), Space: O(?)
def solve_optimal():
    pass

if __name__ == "__main__":
    # Add tests here
    pass
'''

def main():
    # 1. Ensure directories exist
    for topic in TOPICS:
        for diff in DIFFICULTIES:
            os.makedirs(os.path.join(BASE_DIR, "topics", topic, diff), exist_ok=True)
            
    # 2. Write real problems
    for prob in REAL_PROBLEMS:
        filepath = os.path.join(BASE_DIR, "topics", prob["topic"], prob["difficulty"], prob["filename"])
        with open(filepath, "w") as f:
            f.write(prob["content"])
            
    # 3. Generate remaining templates to reach 300
    current_num = 6 # Start from 6 since 1-5 are (or will be) real
    
    # Distribute the rest across topics and difficulties
    files_per_topic = (300 - 5) // len(TOPICS)
    
    for topic in TOPICS:
        for i in range(files_per_topic):
            diff = DIFFICULTIES[i % 3] # Rotate difficulties
            filename = f"{current_num:03d}_template_problem.py"
            filepath = os.path.join(BASE_DIR, "topics", topic, diff, filename)
            
            with open(filepath, "w") as f:
                f.write(TEMPLATE.format(num=current_num, difficulty=diff.capitalize(), topic=topic))
            current_num += 1

    print(f"Generated {current_num - 1} problem files.")

if __name__ == "__main__":
    main()

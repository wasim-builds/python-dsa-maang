import os

BASE_DIR = "/home/wasim/.gemini/antigravity/scratch/python-dsa-maang"

NEW_PROBLEMS = [
    {
        "topic": "01_arrays",
        "difficulty": "medium",
        "filename": "006_maximum_subarray.py",
        "content": '''"""
Problem: Maximum Subarray (Kadane's Algorithm)
Difficulty: Medium
Companies: Amazon, Microsoft, LinkedIn, Google

Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""
from typing import List

# BRUTE FORCE
# Time: O(n^2), Space: O(1)
def maxSubArray_brute(nums: List[int]) -> int:
    max_sum = float('-inf')
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum

# OPTIMAL (Kadane's Algorithm)
# Time: O(n), Space: O(1)
def maxSubArray_optimal(nums: List[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0
    for n in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += n
        max_sum = max(max_sum, curr_sum)
    return max_sum

if __name__ == "__main__":
    assert maxSubArray_optimal([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert maxSubArray_optimal([1]) == 1
    assert maxSubArray_optimal([5,4,-1,7,8]) == 23
    print("✅ All tests passed!")
''',
    },
    {
        "topic": "01_arrays",
        "difficulty": "medium",
        "filename": "007_product_of_array_except_self.py",
        "content": '''"""
Problem: Product of Array Except Self
Difficulty: Medium
Companies: Amazon, Apple, Microsoft

Problem Statement:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from typing import List

# OPTIMAL
# Time: O(n), Space: O(1) (excluding output array)
def productExceptSelf(nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
        
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
        
    return res

if __name__ == "__main__":
    assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
    print("✅ All tests passed!")
''',
    },
    {
        "topic": "03_linked_lists",
        "difficulty": "easy",
        "filename": "008_reverse_linked_list.py",
        "content": '''"""
Problem: Reverse Linked List
Difficulty: Easy
Companies: Amazon, Microsoft, Apple, Google

Problem Statement:
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))
from utils.data_structures import ListNode, list_to_linked, linked_to_list

# OPTIMAL (Iterative)
# Time: O(n), Space: O(1)
def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

if __name__ == "__main__":
    head = list_to_linked([1,2,3,4,5])
    rev_head = reverseList(head)
    assert linked_to_list(rev_head) == [5,4,3,2,1]
    print("✅ All tests passed!")
''',
    },
    {
        "topic": "03_linked_lists",
        "difficulty": "easy",
        "filename": "009_merge_two_sorted_lists.py",
        "content": '''"""
Problem: Merge Two Sorted Lists
Difficulty: Easy
Companies: Amazon, Microsoft, Google

Problem Statement:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. Return the head of the merged linked list.
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))
from utils.data_structures import ListNode, list_to_linked, linked_to_list

# OPTIMAL
# Time: O(n + m), Space: O(1)
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
        
    return dummy.next

if __name__ == "__main__":
    l1 = list_to_linked([1,2,4])
    l2 = list_to_linked([1,3,4])
    merged = mergeTwoLists(l1, l2)
    assert linked_to_list(merged) == [1,1,2,3,4,4]
    print("✅ All tests passed!")
''',
    },
    {
        "topic": "04_stacks_queues",
        "difficulty": "easy",
        "filename": "010_valid_parentheses.py",
        "content": '''"""
Problem: Valid Parentheses
Difficulty: Easy
Companies: Amazon, Microsoft, Meta, Google

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
"""

# OPTIMAL (Stack)
# Time: O(n), Space: O(n)
def isValid(s: str) -> bool:
    stack = []
    closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
    
    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
            
    return True if not stack else False

if __name__ == "__main__":
    assert isValid("()") == True
    assert isValid("()[]{}") == True
    assert isValid("(]") == False
    assert isValid("([)]") == False
    print("✅ All tests passed!")
''',
    },
    {
        "topic": "07_dynamic_programming",
        "difficulty": "easy",
        "filename": "011_climbing_stairs.py",
        "content": '''"""
Problem: Climbing Stairs
Difficulty: Easy
Companies: Amazon, Apple, Microsoft

Problem Statement:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

# OPTIMAL (DP / Fibonacci)
# Time: O(n), Space: O(1)
def climbStairs(n: int) -> int:
    one, two = 1, 1
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
    return one

if __name__ == "__main__":
    assert climbStairs(2) == 2
    assert climbStairs(3) == 3
    assert climbStairs(5) == 8
    print("✅ All tests passed!")
''',
    },
    {
        "topic": "08_binary_search",
        "difficulty": "easy",
        "filename": "012_binary_search.py",
        "content": '''"""
Problem: Binary Search
Difficulty: Easy
Companies: Microsoft, Google, Apple

Problem Statement:
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List

# OPTIMAL
# Time: O(log n), Space: O(1)
def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = l + ((r - l) // 2) # prevents overflow
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
            
    return -1

if __name__ == "__main__":
    assert search([-1,0,3,5,9,12], 9) == 4
    assert search([-1,0,3,5,9,12], 2) == -1
    print("✅ All tests passed!")
''',
    },
]


def main():
    for prob in NEW_PROBLEMS:
        filepath = os.path.join(
            BASE_DIR, "topics", prob["topic"], prob["difficulty"], prob["filename"]
        )
        with open(filepath, "w") as f:
            f.write(prob["content"])
    print(f"Added {len(NEW_PROBLEMS)} real MAANG problems.")


if __name__ == "__main__":
    main()

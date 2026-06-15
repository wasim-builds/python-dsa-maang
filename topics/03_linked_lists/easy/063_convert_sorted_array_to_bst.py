"""
Problem: Convert Sorted Array to Binary Search Tree
Difficulty: Easy
Topic: 03_linked_lists  Companies: Amazon,Microsoft
Problem Statement: Given sorted array in ascending order, return a height-balanced BST.
Complexity: Time O(N), Space O(log N)
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, tree_to_list
from typing import List, Optional


def solve_brute(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = solve_brute(nums[:mid])
    root.right = solve_brute(nums[mid + 1 :])
    return root


def solve_optimal(nums):
    return solve_brute(nums)


if __name__ == "__main__":
    test_cases = [([-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5]), ([1, 3], [3, 1])]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, ex in test_cases:
        assert tree_to_list(solve_optimal(nums)) == ex
    print("All tests passed successfully!")

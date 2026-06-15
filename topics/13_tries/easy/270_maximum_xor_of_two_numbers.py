"""
Problem: Maximum XOR of Two Numbers in an Array
Difficulty: Easy  Companies: Google,Amazon
Problem Statement: Find max XOR of any two numbers in array.
Complexity: Time O(N), Space O(N) trie
"""

from typing import List


def solve_brute(nums):
    res = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            res = max(res, nums[i] ^ nums[j])
    return res


def solve_optimal(nums):
    res = 0
    mask = 0
    for i in range(31, -1, -1):
        mask |= 1 << i
        prefixes = {n & mask for n in nums}
        candidate = res | (1 << i)
        if any(candidate ^ p in prefixes for p in prefixes):
            res = candidate
    return res


if __name__ == "__main__":
    test_cases = [([3, 10, 5, 25, 2, 8], 28)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, ex in test_cases:
        assert solve_brute(nums) == ex
    print("All tests passed successfully!")

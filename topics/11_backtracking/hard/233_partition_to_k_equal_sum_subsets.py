"""
Problem: Partition to K Equal Sum Subsets
Difficulty: Hard  Companies: Amazon,Google,Facebook
Problem Statement: Partition array into k subsets with equal sum.
Complexity: Time O(k * 2^N), Space O(N)
"""

from typing import List


def solve_brute(nums, k):
    return solve_optimal(nums, k)


def solve_optimal(nums, k):
    total = sum(nums)
    if total % k:
        return False
    target = total // k
    nums.sort(reverse=True)
    if nums[0] > target:
        return False
    buckets = [0] * k

    def bt(i):
        if i == len(nums):
            return len(set(buckets)) == 1
        seen = set()
        for j in range(k):
            if buckets[j] in seen:
                continue
            if buckets[j] + nums[i] <= target:
                seen.add(buckets[j])
                buckets[j] += nums[i]
                if bt(i + 1):
                    return True
                buckets[j] -= nums[i]
        return False

    return bt(0)


if __name__ == "__main__":
    test_cases = [([4, 3, 2, 3, 5, 2, 1], 4, True), ([1, 2, 3, 4], 3, False)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, k, ex in test_cases:
        assert solve_optimal(nums, k) == ex
    print("All tests passed successfully!")

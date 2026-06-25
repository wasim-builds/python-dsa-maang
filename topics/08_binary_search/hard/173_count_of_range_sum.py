"""
Problem: Count of Range Sum
Difficulty: Hard  Companies: Google
Problem Statement: Count range sums that lie in [lower, upper] inclusive.
Complexity: Time O(N log N) merge sort, Space O(N)
"""

from typing import List


def solve_brute(nums: List[int], lo: int, hi: int) -> int:
    pre = [0]
    cnt = 0
    for n in nums:
        pre.append(pre[-1] + n)
    for i in range(len(pre)):
        for j in range(i + 1, len(pre)):
            if lo <= pre[j] - pre[i] <= hi:
                cnt += 1
    return cnt


def solve_optimal(nums: List[int], lo: int, hi: int) -> int:
    pre = [0]
    for n in nums:
        pre.append(pre[-1] + n)

    def merge_count(ps):
        if len(ps) <= 1:
            return ps, 0
        mid = len(ps) // 2
        L, lc = merge_count(ps[:mid])
        R, rc = merge_count(ps[mid:])
        count = lc + rc
        j = k = 0
        
        # L and R are sorted prefix sums. For each prefix sum `l` in L,
        # we want to find the number of prefix sums `r` in R such that:
        # lo <= r - l <= hi  =>  lo + l <= r <= hi + l
        # Since R is sorted, we can use two pointers j and k to find the range.
        for l in L:
            while j < len(R) and R[j] - l < lo:
                j += 1
            while k < len(R) and R[k] - l <= hi:
                k += 1
            # k is the first index where R[k] - l > hi
            # j is the first index where R[j] - l >= lo
            # The number of valid elements is k - j
            count += k - j
            
        # Using Timsort here is practically fast, though standard merge is O(N)
        return sorted(L + R), count

    _, ans = merge_count(pre)
    return ans


if __name__ == "__main__":
    test_cases = [([-2, 5, -1], -2, 2, 3), ([], 0, 0, 0)]

    for nums, lo, hi, ex in test_cases:
        assert solve_optimal(nums, lo, hi) == ex
        assert solve_brute(nums, lo, hi) == ex
    print("All tests passed successfully!")

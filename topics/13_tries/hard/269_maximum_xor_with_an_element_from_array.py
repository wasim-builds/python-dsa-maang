"""
Problem: Maximum XOR With an Element From Array
Difficulty: Hard  Companies: Google,Amazon
Problem Statement: For each query [x,m], find max XOR of x with any element <=m.
Complexity: Time O((N+Q) log M), Space O(N)
"""

import pytest
from typing import List


def solve_brute(nums, queries):
    res = []
    for x, m in queries:
        best = -1
        for n in nums:
            if n <= m:
                best = max(best, x ^ n)
        res.append(best)
    return res


def solve_optimal(nums, queries):
    qs = sorted(enumerate(queries), key=lambda x: x[1][1])
    nums_sorted = sorted(nums)
    res = [-1] * len(queries)
    i = 0
    trie = {}

    def insert(n):
        node = trie
        for b in range(31, -1, -1):
            bit = (n >> b) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def query(n):
        node = trie
        xor = 0
        for b in range(31, -1, -1):
            bit = (n >> b) & 1
            want = 1 - bit
            if want in node:
                xor |= 1 << b
                node = node[want]
            elif bit in node:
                node = node[bit]
            else:
                return -1
        return xor

    for qi, (x, m) in qs:
        while i < len(nums_sorted) and nums_sorted[i] <= m:
            insert(nums_sorted[i])
            i += 1
        if trie:
            res[qi] = query(x)
    return res


@pytest.mark.parametrize(
    "nums,q,ex", [([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]], [3, 3, 7])]
)
def test_opt(nums, q, ex):
    assert solve_optimal(nums, q) == ex


@pytest.mark.parametrize(
    "nums,q,ex", [([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]], [3, 3, 7])]
)
def test_brute(nums, q, ex):
    assert solve_brute(nums, q) == ex

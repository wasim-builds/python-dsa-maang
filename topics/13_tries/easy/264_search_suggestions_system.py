"""
Problem: Search Suggestions System
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Return 3 products suggestion list for each prefix of searchWord.
Complexity: Time O(N log N + M^2), Space O(N)
"""

import pytest
from typing import List
import bisect


def solve_brute(products, searchWord):
    return solve_optimal(products, searchWord)


def solve_optimal(products, searchWord):
    products.sort()
    res = []
    prefix = ""
    for c in searchWord:
        prefix += c
        i = bisect.bisect_left(products, prefix)
        res.append([p for p in products[i : i + 3] if p.startswith(prefix)])
    return res


@pytest.mark.parametrize(
    "p,sw,ex",
    [
        (
            ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
            "mouse",
            [
                ["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
            ],
        )
    ],
)
def test_opt(p, sw, ex):
    assert solve_optimal(p, sw) == ex

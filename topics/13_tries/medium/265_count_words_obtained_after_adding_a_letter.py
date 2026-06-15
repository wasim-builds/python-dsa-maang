"""
Problem: Map Sum Pairs (Trie Map)
Difficulty: Medium  Companies: Amazon,Google
Problem Statement: Implement Trie-based map with prefix sum functionality.
Complexity: Time O(K) insert/sum, Space O(N * K)
"""

import pytest


class MapSum:
    def __init__(self):
        self.map = {}
        self.trie = {}

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        curr = self.trie
        for c in key:
            if c not in curr:
                curr[c] = {"_sum": 0}
            curr[c]["_sum"] += delta
            curr = curr[c]

    def sum(self, prefix):
        curr = self.trie
        for c in prefix:
            if c not in curr:
                return 0
            curr = curr[c]
        return curr.get("_sum", 0)


def test_mapsum():
    m = MapSum()
    m.insert("apple", 3)
    assert m.sum("ap") == 3
    m.insert("app", 2)
    assert m.sum("ap") == 5

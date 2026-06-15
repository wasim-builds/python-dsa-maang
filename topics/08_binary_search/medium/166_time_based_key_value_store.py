"""
Problem: Time Based Key-Value Store
Difficulty: Medium  Companies: Google,Amazon,Facebook,Uber
Problem Statement: Design time-based key-value data structure that can store multiple values at different timestamps.
Complexity: Time O(log N) get, Space O(N)
"""

import pytest
from collections import defaultdict
import bisect


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key, val, ts):
        self.store[key].append((ts, val))

    def get(self, key, ts):
        if key not in self.store:
            return ""
        arr = self.store[key]
        idx = bisect.bisect_right(arr, (ts, chr(127))) - 1
        return arr[idx][1] if idx >= 0 else ""


def test_timemap():
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"
    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"

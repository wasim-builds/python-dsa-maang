"""
Problem: Random Pick with Weight
Difficulty: Hard  Companies: Google,Lyft,Facebook,Amazon
Problem Statement: Pick index with probability proportional to its weight.
Complexity: Time O(log N) pick, Space O(N)
"""

import random, bisect
from typing import List


class Solution:
    def __init__(self, w):
        self.prefix = [0]
        for x in w:
            self.prefix.append(self.prefix[-1] + x)

    def pickIndex(self):
        total = self.prefix[-1]
        r = random.randint(1, total)
        return bisect.bisect_left(self.prefix, r) - 1


if __name__ == "__main__":
    s = Solution([1, 3])
    counts = {0: 0, 1: 0}
    for _ in range(1000):
        counts[s.pickIndex()] += 1
    assert counts[1] > counts[0]
    print("All tests passed successfully!")

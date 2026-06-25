"""
Problem: Beautiful Arrangement
Difficulty: Hard  Companies: Google,Amazon
Problem Statement: Count beautiful arrangements where nums[i]%i==0 or i%nums[i]==0 for each 1-indexed position.
Complexity: Time O(k) where k is valid placements, Space O(N)
"""


def solve_brute(n):
    return solve_optimal(n)


def solve_optimal(n):
    count = [0]
    used = [False] * (n + 1)

    def bt(pos):
        if pos > n:
            count[0] += 1
            return
        for i in range(1, n + 1):
            if not used[i] and (i % pos == 0 or pos % i == 0):
                used[i] = True
                bt(pos + 1)
                used[i] = False

    bt(1)
    return count[0]


if __name__ == "__main__":
    test_cases = [(2, 2), (1, 1), (3, 3)]

    for n, ex in test_cases:
        assert solve_optimal(n) == ex
    print("All tests passed successfully!")

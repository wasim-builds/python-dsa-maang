"""
Problem: Lemonade Change
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Return true if can provide change for each customer (5,10,20 bills).
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(bills):
    return solve_optimal(bills)


def solve_optimal(bills):
    five = ten = 0
    for b in bills:
        if b == 5:
            five += 1
        elif b == 10:
            if not five:
                return False
            five -= 1
            ten += 1
        else:
            if ten and five:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True


if __name__ == "__main__":
    test_cases = [([5, 5, 5, 10, 20], True), ([5, 5, 10, 10, 20], False)]

    for b, ex in test_cases:
        assert solve_optimal(b) == ex
    print("All tests passed successfully!")

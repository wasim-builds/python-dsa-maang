"""
Problem: Climbing Stairs
Difficulty: Easy
Companies: Amazon, Apple, Microsoft

Problem Statement:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

# OPTIMAL (DP / Fibonacci)
# Time: O(n), Space: O(1)
def climbStairs(n: int) -> int:
    one, two = 1, 1
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
    return one

if __name__ == "__main__":
    assert climbStairs(2) == 2
    assert climbStairs(3) == 3
    assert climbStairs(5) == 8
    print("✅ All tests passed!")

"""
Problem: Climbing Stairs
Difficulty: Easy
Companies: Amazon, Apple, Microsoft

Problem Statement:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Complexity Proof:
- Time Complexity: O(N) because we have a single loop running N times to compute the Fibonacci sequence.
- Space Complexity: O(1) because we only need to store the previous two values (`one` and `two`) rather than a full DP array of size N.
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
    test_cases = [(2, 2), (3, 3), (5, 8)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for n, expected in test_cases:
        assert climbStairs(n) == expected
    print("All tests passed successfully!")

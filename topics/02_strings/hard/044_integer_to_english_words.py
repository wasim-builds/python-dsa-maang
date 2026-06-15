"""
Problem: Integer to English Words
Difficulty: Hard
Topic: 02_strings  Companies: Microsoft,Amazon,Google,Facebook
Problem Statement: Convert non-negative integer to English words.
Complexity: Time O(log N), Space O(log N)
"""

import pytest


def solve_brute(num):
    return solve_optimal(num)


def solve_optimal(num):
    if num == 0:
        return "Zero"
    ones = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]
    tens = [
        "",
        "",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]

    def helper(n):
        if n == 0:
            return ""
        elif n < 20:
            return ones[n] + " "
        elif n < 100:
            return tens[n // 10] + " " + helper(n % 10)
        else:
            return ones[n // 100] + " Hundred " + helper(n % 100)

    parts = ["", "Thousand ", "Million ", "Billion "]
    res = ""
    i = 0
    while num > 0:
        if num % 1000:
            res = helper(num % 1000) + parts[i] + res
        num //= 1000
        i += 1
    return res.strip()


@pytest.mark.parametrize(
    "n,ex",
    [
        (123, "One Hundred Twenty Three"),
        (12345, "Twelve Thousand Three Hundred Forty Five"),
        (1000010, "One Million Ten"),
    ],
)
def test_opt(n, ex):
    assert solve_optimal(n) == ex

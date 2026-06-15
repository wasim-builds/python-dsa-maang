"""
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy
Companies: Amazon, Apple, Google, Meta, Microsoft

Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Complexity Proof:
- Time Complexity: O(N) because we only make a single pass through the prices array.
- Space Complexity: O(1) because we only use two variables (`min_price` and `max_profit`) regardless of the array size.
"""

from typing import List
import pytest


# BRUTE FORCE
# Time: O(n^2), Space: O(1)
def maxProfit_brute(prices: List[int]) -> int:
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit


# OPTIMAL
# Time: O(n), Space: O(1)
def maxProfit_optimal(prices: List[int]) -> int:
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_maxProfit_optimal(prices, expected):
    assert maxProfit_optimal(prices) == expected


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_maxProfit_brute(prices, expected):
    assert maxProfit_brute(prices) == expected

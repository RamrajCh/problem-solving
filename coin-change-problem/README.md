# Coin Change Problem

## Problem Statement

Given a set of coin denominations and a target sum, find the minimum number of coins needed to make the target sum.

## Examples
- Given the coin denominations `[1, 5, 10]` and a target sum of `22`, the minimum number of coins needed is `4` (2 x 10-coin denominations and 2 x 1-coin denominations)

- Given the coin denominations `[1, 2, 5]` and a target sum of `12`, the minimum number of coins needed is `5` (5 x 2-coin denominations and 1 x 2-coin denomination)

## Method of solving the problem

- **Brute force method**, which involves generating all possible combinations of coins and checking each one to see if it adds up to the target sum. This method can be very time-consuming and inefficient for large sets of coin denominations and target sums.

- **Greedy Algorithm**, it's a simple approach where we select the coin denomination which is closest to the target sum, it's not always correct but it's fast and easy to implement, it's good to use it as a heuristic.

- **Dynamic programming method**, which involves breaking the problem down into smaller subproblems and storing the solutions to those subproblems in a table, so they can be reused later. This method is more efficient than the brute force method, but it can be more complex to implement.
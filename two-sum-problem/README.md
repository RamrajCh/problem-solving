# Two Sum Problem
The Two Sum Problem is a common problem in computer science, where the goal is to find two integers from a given list of integers that add up to a target value. This problem can be useful in various scenarios, such as in financial applications where the goal is to find two transactions that add up to a specific amount.

___

## Problem Description
Given a list of integers and a target value, find two integers from the list that add up to the target value. If no such integers exist, return None.

### Examples

**Input**: `[1, 2, 3, 4, 5], 5`

**Output**: `(2, 3)` or `(1,4)`

**Input**: `[1, 3, 5, 7, 9], 8`

**Output**: `(1, 7)`

___

## Solution
The Two Sum Problem can be solved using various techniques such as Hash table, Two Pointers, and Brute force.

### Hash Table
One approach to solve this problem is to use a hash table. The idea is to iterate through the list and for each element, check if the difference between the target and the current element exists in the hash table. If it does, you have found the pair and you can return them, otherwise you add the current element to the hash table. This approach has a time complexity of O(n) and a space complexity of O(n).

### Two Pointers
Another approach to solve this problem is to use two pointers. The idea is to sort the list and then use two pointers, one pointing to the beginning of the list and the other pointing to the end. If the sum of the two elements pointed by the pointers is equal to the target, return the pair. If the sum is less than the target, move the left pointer to the right, otherwise move the right pointer to the left. This approach also has a time complexity of O(n) but space complexity of O(1).

### Brute Force
The brute force approach would be to check every possible pair of integers in the list. It has a time complexity of O(n^2) and space complexity of O(1).

# Find the second largest element in an array

## Problem statement
Given an array of integers, write an algorithm to find the second largest element in the array. Your solution should have a time complexity of O(n) and should not use any additional data structures or sorting.

## Method 1: Linear Search
This algorithm iterates through the array once, keeping track of the maximum and second maximum elements as it goes. It has a time complexity of O(n) and does not use any additional data structures or sorting.

## Method 2: Linear Search
This algorithm iterates through the array twice, first finds the maximum element and then iterates again to find the second maximum element. It has a time complexity of O(n) and does not use any additional data structures or sorting.

## Method 3: Sorting-based
This algorithm sorts the array in descending order, and then returns the second element in the sorted array. It has a time complexity of O(nlogn) and uses an additional data structure, the array, which takes O(n) space
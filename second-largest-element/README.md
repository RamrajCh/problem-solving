# Find the second largest element in an array

## Problem statement
Given an array of integers, write an algorithm to find the second largest element in the array.

## Method 1: Linear Search
This algorithm iterates through the array once, keeping track of the maximum and second maximum elements as it goes. It has a time complexity of O(n) and does not use any additional data structures or sorting.

## Method 2: Linear Search
This algorithm iterates through the array twice, first finds the maximum element and then iterates again to find the second maximum element. It has a time complexity of O(n) and does not use any additional data structures or sorting.

## Method 3: Sorting-based
This algorithm sorts the array in descending order, and then returns the second element in the sorted array. The time complexity depends on the sorting algorithm used. For this problem, if bubble sort is used the time complexity would be O(n<sup>2</sup>)
# Word Frequency Counter

## Problem Statement:
Given a string, the program should return a dictionary containing the frequency of each word in the string. The keys of the dictionary should be the words and the values should be the number of times each word appears in the input string. The program should be case-insensitive and ignore punctuation.

## Examples:

Input: `"Hello, World! This is a test."`

Output:
```py
{
    'hello': 1,
    'world': 1,
    'this': 1,
    'is': 1,
    'a': 1,
    'test': 1
}
```

Input: `"This is a test. This is only a test."`

Output:
```py
{
    'this': 2,
    'is': 2,
    'a': 2,
    'test': 2,
    'only': 1,
}
```
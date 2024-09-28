Here's the README.md for the "Longest Substring Without Repeating Characters" problem:

# Longest Substring Without Repeating Characters

## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

### Example 1:
- **Input**: `s = "abcabcbb"`
- **Output**: `3`
- **Explanation**: The answer is "abc", with the length of 3.

### Example 2:
- **Input**: `s = "bbbbb"`
- **Output**: `1`
- **Explanation**: The answer is "b", with the length of 1.

### Example 3:
- **Input**: `s = "pwwkew"`
- **Output**: `3`
- **Explanation**: The answer is "wke", with the length of 3.
  - Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Constraints:
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces.

## Solution Explanation
The solution uses a sliding window approach to efficiently find the longest substring without repeating characters. The algorithm maintains a window defined by two pointers, `l` and `r`, where `l` is the left pointer and `r` is the right pointer. As the right pointer expands, the algorithm checks if the character has already been seen within the current window. If a repeating character is found, the left pointer moves past the last occurrence of this character to ensure no repeats. The length of the current window is tracked and compared to find the maximum length of any such substring.

### Time Complexity
- **O(n)**: The algorithm processes each character of the string exactly once, where `n` is the length of the string.

### Space Complexity
- **O(min(m, n))**: The space complexity is proportional to the size of the character set `m` (for example, 128 for ASCII characters) and the length of the string `n`.

## Test Cases
The following test cases are included and can be run using `pytest`:

1. **Example case 1**: `s = "abcabcbb"` -> Output: `3`
2. **Example case 2**: `s = "bbbbb"` -> Output: `1`
3. **Example case 3**: `s = "pwwkew"` -> Output: `3`
4. **Edge case with an empty string**: `s = ""` -> Output: `0`
5. **Edge case with a single character**: `s = "a"` -> Output: `1`
6. **All unique characters**: `s = "abcdef"` -> Output: `6`
7. **String with repeating characters**: `s = "aab"` -> Output: `2`
8. **Complex case**: `s = "dvdf"` -> Output: `3`
9. **String with numbers and symbols**: `s = "123@321"` -> Output: `4`

## Running Tests

To run the tests, ensure you have `pytest` installed and run:

```bash
pytest test.py
```

This README.md provides a clear and concise description of the problem, the solution, and how to run the tests, following the same structure as the example README.md you provided.
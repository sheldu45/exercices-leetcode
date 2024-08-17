# Two Sum

## Problem Description
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Example 1:
- **Input**: `nums = [2, 7, 11, 15], target = 9`
- **Output**: `[0, 1]`
- **Explanation**: Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

### Example 2:
- **Input**: `nums = [3, 2, 4], target = 6`
- **Output**: `[1, 2]`

### Example 3:
- **Input**: `nums = [3, 3], target = 6`
- **Output**: `[0, 1]`

### Constraints:
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Solution Explanation
The solution uses a dictionary to store each number and its corresponding index as we iterate through the array. For each number, we calculate its complement (i.e., `target - num`). If the complement is found in the dictionary, we return the indices.

### Time Complexity
- **O(n)**: We pass through the list only once.

### Space Complexity
- **O(n)**: We store the numbers in a dictionary.

## Test Cases
The following test cases are included and can be run using `pytest`:

1. **Example case**: `nums = [2, 7, 11, 15], target = 9` -> Output: `[0, 1]`
2. **Case with repeated numbers**: `nums = [3, 2, 4], target = 6` -> Output: `[1, 2]`
3. **Case with negative numbers**: `nums = [3, 3], target = 6` -> Output: `[0, 1]`

## Running Tests

To run the tests, ensure you have `pytest` installed and run:

```bash
pytest test.py
```

*Note: Please refer to the root `README.md` for instructions on how to set up a virtual environment and install `pytest` using `requirements.txt`.*
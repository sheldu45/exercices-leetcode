# Add Two Numbers

## Problem Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zeros, except the number 0 itself.

### Example 1:
- **Input**: `l1 = [2, 4, 3]`, `l2 = [5, 6, 4]`
- **Output**: `[7, 0, 8]`
- **Explanation**: 342 + 465 = 807, which is represented as [7, 0, 8] in reverse order.

### Example 2:
- **Input**: `l1 = [0]`, `l2 = [0]`
- **Output**: `[0]`

### Example 3:
- **Input**: `l1 = [9, 9, 9, 9, 9, 9, 9]`, `l2 = [9, 9, 9, 9]`
- **Output**: `[8, 9, 9, 9, 0, 0, 0, 1]`
- **Explanation**: 9999999 + 9999 = 10009998, which is represented as [8, 9, 9, 9, 0, 0, 0, 1] in reverse order.

### Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

## Solution Explanation
The solution iterates through both linked lists simultaneously, summing the corresponding digits along with any carry from the previous step. The sum of each pair of digits (along with the carry) is stored in a new node of the resulting linked list. The process continues until both linked lists are fully traversed. If there's a remaining carry after the last digits are processed, it's added as an additional node at the end.

### Time Complexity
- **O(max(m, n))**: The algorithm iterates through the linked lists, with `m` and `n` being the lengths of `l1` and `l2`, respectively. The time complexity is proportional to the length of the longer list.

### Space Complexity
- **O(max(m, n))**: The space complexity is proportional to the length of the longer linked list, as the output linked list needs to store all digits of the result.

## Test Cases
The following test cases are included and can be run using `pytest`:

1. **Example case**: `l1 = [2, 4, 3]`, `l2 = [5, 6, 4]` -> Output: `[7, 0, 8]`
2. **Case with zero nodes**: `l1 = [0]`, `l2 = [0]` -> Output: `[0]`
3. **Case with carry propagation**: `l1 = [9, 9, 9, 9, 9, 9, 9]`, `l2 = [9, 9, 9, 9]` -> Output: `[8, 9, 9, 9, 0, 0, 0, 1]`

## Running Tests

To run the tests, ensure you have `pytest` installed and run:

```bash
pytest test.py

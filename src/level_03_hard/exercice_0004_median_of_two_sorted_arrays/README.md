# Median of Two Sorted Arrays

## Problem Description
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall runtime complexity should be `O(log(m + n))`.

### Example 1:
- **Input**: `nums1 = [1, 3]`, `nums2 = [2]`
- **Output**: `2`
- **Explanation**: The merged array is `[1, 2, 3]` and the median is `2`.

### Example 2:
- **Input**: `nums1 = [1, 2]`, `nums2 = [3, 4]`
- **Output**: `2.5`
- **Explanation**: The merged array is `[1, 2, 3, 4]` and the median is `(2 + 3) / 2 = 2.5`.

### Constraints:
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Solution Explanation
The solution uses a binary search approach to find the median of two sorted arrays without merging them. The algorithm performs a binary search on the smaller of the two arrays to find the correct partition that divides the combined array into two halves where all elements on the left are less than or equal to all elements on the right.

### Steps:
1. **Partitioning the Arrays**: We find a partition index in both arrays such that the left part of the combined array contains elements less than or equal to those in the right part.
2. **Adjusting the Binary Search**: If the partition is not correct (i.e., the largest element in the left part is greater than the smallest element in the right part), adjust the partition using binary search.
3. **Calculating the Median**: Once the correct partition is found:
   - If the total number of elements is odd, the median is the largest element in the left partition.
   - If the total number of elements is even, the median is the average of the largest element in the left partition and the smallest element in the right partition.

### Time Complexity
- **O(log(min(m, n)))**: The binary search runs on the smaller array, reducing the search space logarithmically.

### Space Complexity
- **O(1)**: The algorithm uses a constant amount of extra space.

## Test Cases
The following test cases are included and can be run using `pytest`:

1. **Example case 1**: `nums1 = [1, 3]`, `nums2 = [2]` -> Output: `2`
2. **Example case 2**: `nums1 = [1, 2]`, `nums2 = [3, 4]` -> Output: `2.5`
3. **Both arrays empty**: `nums1 = []`, `nums2 = []` -> Output: `ValueError`
4. **One array empty**: `nums1 = []`, `nums2 = [1]` -> Output: `1`
5. **Both arrays of different sizes**: `nums1 = [1, 3, 5]`, `nums2 = [2, 4, 6, 7]` -> Output: `4`
6. **Arrays with duplicate elements**: `nums1 = [1, 2, 2]`, `nums2 = [2, 3, 4]` -> Output: `2`
7. **Arrays with negative numbers**: `nums1 = [-5, -3, -1]`, `nums2 = [-2, 0, 2, 4]` -> Output: `-1.5`
8. **One array is larger than the other**: `nums1 = [1, 2, 3, 4, 5]`, `nums2 = [6, 7, 8, 9, 10, 11]` -> Output: `5.5`

## Running Tests

To run the tests, ensure you have `pytest` installed and run:

```bash
pytest test.py
```
import pytest
from solution import Solution

def test_example_case_1():
    solution = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 2.0

def test_example_case_2():
    solution = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 2.5

def test_single_element_each():
    solution = Solution()
    nums1 = [1]
    nums2 = [2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 1.5

def test_empty_first_array():
    solution = Solution()
    nums1 = []
    nums2 = [1, 2, 3]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 2.0

def test_empty_second_array():
    solution = Solution()
    nums1 = [1, 2, 3]
    nums2 = []
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 2.0

def test_different_lengths():
    solution = Solution()
    nums1 = [1, 3, 8]
    nums2 = [7, 9]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 7.0

def test_negative_numbers():
    solution = Solution()
    nums1 = [-5, 3, 6]
    nums2 = [-2, 4, 8]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 3.5

def test_all_negative():
    solution = Solution()
    nums1 = [-7, -3, -1]
    nums2 = [-6, -4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == -4.0

def test_large_arrays():
    solution = Solution()
    nums1 = list(range(1000))
    nums2 = list(range(1000, 2000))
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 999.5

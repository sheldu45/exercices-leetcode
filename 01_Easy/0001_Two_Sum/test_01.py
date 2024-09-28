import pytest
from solution import Solution

def test_example_case():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]

def test_another_case():
    solution = Solution()
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]

def test_negative_numbers():
    solution = Solution()
    assert solution.twoSum([3, 3], 6) == [0, 1]


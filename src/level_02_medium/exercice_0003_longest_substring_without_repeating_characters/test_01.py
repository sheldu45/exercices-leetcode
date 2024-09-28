import pytest
from src.level_02_medium.exercice_0003_longest_substring_without_repeating_characters.solution import Solution

def test_example_case_1():
    solution = Solution()
    s = "abcabcbb"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 3

def test_example_case_2():
    solution = Solution()
    s = "bbbbb"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 1

def test_example_case_3():
    solution = Solution()
    s = "pwwkew"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 3

def test_empty_string():
    solution = Solution()
    s = ""
    result = solution.lengthOfLongestSubstring(s)
    assert result == 0

def test_single_character():
    solution = Solution()
    s = "a"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 1

def test_all_unique():
    solution = Solution()
    s = "abcdef"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 6

def test_repeating_characters():
    solution = Solution()
    s = "aab"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 2

def test_complex_case():
    solution = Solution()
    s = "dvdf"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 3

def test_numbers_and_symbols():
    solution = Solution()
    s = "123@321"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 4

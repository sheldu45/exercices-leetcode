import pytest
from src.level_02_medium.exercice_0002_add_two_numbers.solution import Solution, ListNode

def list_to_linkedlist(lst):
    # Helper function to convert list to linked list
    dummy_head = ListNode(0)
    current = dummy_head
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy_head.next

def linkedlist_to_list(node):
    # Helper function to convert linked list to list
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_example_case():
    solution = Solution()
    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [7, 0, 8]

def test_zero_case():
    solution = Solution()
    l1 = list_to_linkedlist([0])
    l2 = list_to_linkedlist([0])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [0]

def test_carry_propagation():
    solution = Solution()
    l1 = list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linkedlist([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]

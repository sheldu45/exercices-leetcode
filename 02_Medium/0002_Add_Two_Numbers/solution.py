# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2:
            # Extract values from the current nodes or use 0 if the node is missing
            lv = l1.val if l1 else 0
            rv = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = lv + rv + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes in the list, if available
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next
        
        # If carry is still present after the loop, create a new node for it
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the head of the resultant linked list
        return dummy_head.next
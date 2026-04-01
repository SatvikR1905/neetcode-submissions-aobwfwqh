# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 # to take sum > 9
        dummy = ListNode(0) # caz we are creating new list (not technically but you do get it. to build result)
        curr = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 # handling edge cases what if l1 is none
            v2 = l2.val if l2 else 0 
            total = v1 + v2 + carry
            digit = total % 10 # takes ones place and move carryover
            carry = total // 10
            curr.next = ListNode(digit) # we create nodes and keep adding the digits
            curr = curr.next #increment the current
            l1 = l1.next if l1 else None #move l1 and l2
            l2 = l2.next if l2 else None
        return dummy.next


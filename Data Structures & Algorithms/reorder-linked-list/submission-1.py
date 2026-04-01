# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None # because when we reverse the half we can see that slow.next still is connected (6 -> 8)
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second = prev
        

        first = head
        while second: # because second half is always shorter than first 
            tmp1 = first.next # we copy it before we loose
            tmp2 = second.next # we copy it before we loose
            first.next = second # we interchange the references
            second.next = tmp1
            first = tmp1 # we move the pointer to next
            second = tmp2
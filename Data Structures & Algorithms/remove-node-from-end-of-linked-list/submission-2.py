# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0) #we create a dummy node as we might encounter deletion of head
        dummy.next = head #dummy_next points to head
        slow = dummy # both pointers start from dummy
        fast = dummy

        for i in range(n+1): # if we do for n then the slow pointer points to the exact node we are pointing to
            fast = fast.next # we move fast (n+1) steps ahead (so in arrays we can move directly to that index but in linked list you have to traverse in one way)
        
        while fast: # till while hits none you increment the pointers
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next # you skip the nth node and point to next
        return dummy.next
        
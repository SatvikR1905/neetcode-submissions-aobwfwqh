# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        dummy.next = head

        while True:
            kth = self.getkth(prev,k)
            if not kth:
                break

            groupstart = prev.next
            nextgroup = kth.next

            kth.next = None
            self.reverse(groupstart)

            prev.next = kth
            groupstart.next = nextgroup

            prev = groupstart
        return dummy.next



    def getkth(self,curr,k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverse(self,head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

        
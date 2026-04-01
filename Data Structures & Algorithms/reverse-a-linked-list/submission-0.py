# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next #it should hold the value of next before we loose it
            curr.next = prev # we point curr back
            prev = curr # move the prev front
            curr = next_node # move the current also front
        return prev
        
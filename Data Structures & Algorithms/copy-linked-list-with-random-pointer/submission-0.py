"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None:None} #handling the edge case where when random points to None
        curr = head

        #pass 1 create all nodes in hashmap first (we might need to point the random pointer to a node which has not been created yet)
        while curr:
            hashmap[curr] = Node(curr.val) #create a node in hashmap of curr.val
            curr = curr.next
        
        #pass 2 Connect all pointers
        curr = head
        while curr:
            hashmap[curr].next = hashmap[curr.next]
            hashmap[curr].random = hashmap[curr.random]
            curr = curr.next

        return hashmap[head] #we need to return new node

        
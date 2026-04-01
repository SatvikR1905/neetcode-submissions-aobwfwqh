"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: # if there is no ned then return None
            return None

        hashmap = {} # to store mapping of original to clone

        def dfs(node):
            if node in hashmap:
                return hashmap[node] #if it exist then return from the map
            
            clone = Node(node.val) #clone the value
            hashmap[node] = clone    #Store it in hashmap

            for neighbor in node.neighbors: # for every neighbor clone adn append it to list
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)
        
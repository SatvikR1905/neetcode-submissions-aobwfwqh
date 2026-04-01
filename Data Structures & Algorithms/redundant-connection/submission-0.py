class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # Every node is parent of his starting up
        parent={}
        for i in range(1,len(edges)+1):
            parent[i] = i
        
        #This is for finding the root of node
        def find(node):
            if parent[node] != node: 
                parent[node] = find(parent[node]) #recursive call to find the parent node
            return parent[node]

        def union(a,b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB: #if its same it forms cycle
                return False

            parent[rootA] = rootB # merging two groups 
            return True

        for a , b in edges: # we loop through the edges and see which combination is the reason for formation of cycle
            if not union(a,b):
                return [a,b]


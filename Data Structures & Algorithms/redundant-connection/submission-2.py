class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1)) #everyone is parent of themselves

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        def union(x,y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return (x,y)
            else:
                parent[root_x] = root_y #assigning the parent if the parents dont match 

        for a , b in edges:
            if union(a,b) != None:
                return [a , b]

        

        
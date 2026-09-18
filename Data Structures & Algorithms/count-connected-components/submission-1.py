class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = n
        parent = list(range(n))

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        def union(x,y):
            nonlocal count
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            else:
                parent[root_x] = root_y
                count -= 1
                return True
        
        for a , b in edges:
            union(a,b)
        return count
                
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = []
        for i in range(len(edges) + 1):
            parent.append(i)

        rank = [1] * (len(edges) + 1)

        def find(node): # to find the parent node
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(a,b): # to merge the groups
            p1 = find(a)
            p2 = find(b)
            if p1 == p2:
                return False

            if rank[p2] > p1:
                parent[p2] = p1
                rank[p2] += rank[p1]
            else:
                parent[p1] = p2
                rank[p1] += rank[p2]
                return True

        for a , b in edges:
            if not union(a,b):
                return [a,b]

        
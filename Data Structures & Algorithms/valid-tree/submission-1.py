class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False

        hashSet = {}
        for i in range(n):
            hashSet[i] = []
        for par , neigh in edges:
            hashSet[par].append(neigh)
            hashSet[neigh].append(par)
        
        visit = set()
        def dfs(node):
            visit.add(node)
            for neigh in hashSet[node]:
                if neigh not in visit:
                    dfs(neigh)
        dfs(0)
        
        return len(visit) == n
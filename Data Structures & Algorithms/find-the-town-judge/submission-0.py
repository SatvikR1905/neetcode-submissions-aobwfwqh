class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = {}
        for i in range(1,n+1):
            graph[i] = []
        for a , b in trust:
            graph[a].append(b)
        
        # first make it incoming as o and then increment
        incoming = {}
        for i in range(1,n+1):
            incoming[i] = 0

        for node in graph: #graph={node:neighbor}
            for neighbor in graph[node]:
                incoming[neighbor] += 1 # how many of them trust the town Judge

        for node in graph:
            if graph[node] == [] and incoming[node] == n-1: # these are the two conditions to satisfy to become town Judge
                return node
        return -1
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {} # create a unidirected graph
        for i in range(n):
            graph[i] = []

        for a , b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            visited.add(node) # marking it as visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
                
        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
        return count
            

        
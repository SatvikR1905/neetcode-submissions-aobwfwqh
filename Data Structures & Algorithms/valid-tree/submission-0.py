class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check the number of edges if its not equal to n-1 then we return false
        if len(edges) != n - 1:
            return False

        #build uidirected graph
        graph = {}
        for i in range(n):
            graph[i] = []

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        #for connectivity
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)

        return len(visited) == n #this is to check if the nodes are connected or not

        
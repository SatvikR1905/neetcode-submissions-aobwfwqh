class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for a , b in prerequisites:
            graph[a].append(b)
        # EX: # prerequisites = [[0,1],[1,2],[2,3]]
        #graph = {
#     0: [1]   ← course 0 needs course 1
#     1: [2]   ← course 1 needs course 2
#     2: [3]   ← course 2 needs course 3
#     3: []    ← course 3 needs nothing
# }
        visiting = set()
        visited = set()

        def dfs(node):
            if node in visiting:
                return False #cycle and infinite loop
            if node in visited:
                return True
            
            visiting.add(node)

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            visiting.remove(node)
            visited.add(node)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
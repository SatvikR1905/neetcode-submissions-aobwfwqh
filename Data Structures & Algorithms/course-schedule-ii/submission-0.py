class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for a , b in prerequisites:
            graph[a].append(b)

        visiting = set()
        visited = set()
        output = []

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
               
            visiting.remove(node)
            visited.add(node)
            output.append(node)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return output

        
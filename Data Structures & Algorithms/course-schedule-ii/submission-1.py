class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course , prereq in prerequisites:
            graph[prereq].append(course)

        white , gray , black = 0 , 1 , 2
        state = [white] * numCourses
        order = []

        def dfs(node):
            if state[node] == gray:
                return True
            if state[node] == black:
                return False

            state[node] = gray
            for neighbour in graph[node]:
                if dfs(neighbour):
                    return True
            state[node] = black
            order.append(node)
            return False

        for node in range(numCourses):
            if state[node] == white and dfs(node):
                return []
        return order[::-1]


        
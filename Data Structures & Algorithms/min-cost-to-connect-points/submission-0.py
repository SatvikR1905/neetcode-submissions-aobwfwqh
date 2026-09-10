class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        total_cost = 0
        min_heap = [(0,0)]

        while len(visited) < n:
            cost , node = heapq.heappop(min_heap)
            if node in visited:
                continue    
            visited.add(node)
            total_cost += cost
            for neighbor in range(n):
                if neighbor in visited:
                    continue
                x1 , y1 = points[node]
                x2 , y2 = points[neighbor]
                dist = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(min_heap, (dist, neighbor))
        return total_cost
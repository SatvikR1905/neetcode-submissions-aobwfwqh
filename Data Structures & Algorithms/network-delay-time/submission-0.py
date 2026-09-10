class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u , v , w in times:
            graph[u].append((v,w))
        min_heap = [(0,k)]
        visited = set()
        max_time = 0
        
        while min_heap:
            dist , node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            max_time = max(max_time , dist)

            for neighbor , weight in graph[node]:
                heapq.heappush(min_heap, (dist + weight , neighbor))
                
        if len(visited) == n:
            return max_time
        else:
            return - 1

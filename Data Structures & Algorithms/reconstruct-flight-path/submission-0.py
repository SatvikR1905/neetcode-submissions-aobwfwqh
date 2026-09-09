class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src , dst in tickets:
            heapq.heappush(graph[src], dst)

        result = []
        def dfs(airport):
            heap = graph[airport]
            while heap:
                next_airport = heapq.heappop(heap)
                dfs(next_airport)
            result.append(airport)
        
        dfs("JFK")
        return result[::-1]

        
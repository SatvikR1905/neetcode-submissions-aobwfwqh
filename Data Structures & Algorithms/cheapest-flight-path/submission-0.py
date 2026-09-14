class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float('inf')] * n
        cost[src] = 0

        for i in range(k+1):
            new_cost = cost.copy()
            for u , v , price in flights:
                if cost[u] != float('inf') and cost[u] + price < new_cost[v]:
                    new_cost[v] = cost[u] + price
            cost = new_cost
        
        if cost[dst] == float('inf'):
            return -1
        else:
            return cost[dst]

        
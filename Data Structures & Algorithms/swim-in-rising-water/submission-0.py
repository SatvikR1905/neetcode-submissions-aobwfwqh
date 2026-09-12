class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        min_heap = [(grid[0][0] , 0 , 0)]
        max_elevation_so_far = 0

        while min_heap:
            elevation , row , col = heapq.heappop(min_heap)
            if (row , col) in visited:
                continue
            visited.add((row,col))
            max_elevation_so_far = max(elevation ,max_elevation_so_far)
            if (row , col) == (n-1,n-1):
                return max_elevation_so_far
            else:
                for dr , dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nr , nc = row + dr , col + dc
                    if nr < 0 or nr >= n or nc < 0 or nc >= n:
                        continue
                    else:
                        heapq.heappush(min_heap , [grid[row+dr][col + dc] , nr , nc])
        
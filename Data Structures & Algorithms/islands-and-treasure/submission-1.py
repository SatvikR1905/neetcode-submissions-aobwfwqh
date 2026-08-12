class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append([row,col])
        
        while q:
           row , col = q.popleft()
           for dr , dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            r = row + dr
            c = col + dc

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == -1 or grid[r][c] != 2147483647:
                continue

            grid[r][c] = grid[row][col] + 1
            q.append((r,c))

        
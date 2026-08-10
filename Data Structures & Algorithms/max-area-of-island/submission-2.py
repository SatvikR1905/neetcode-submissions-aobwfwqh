class Solution:
    def dfs(self,grid,row,col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
            return 0
        
        grid[row][col] = 0

        return 1 + self.dfs(grid,row+1,col) + self.dfs(grid,row-1,col) + self.dfs(grid,row,col+1) + self.dfs(grid,row,col-1)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    area = self.dfs(grid,row,col)
                    max_area = max(max_area,area)

        return max_area

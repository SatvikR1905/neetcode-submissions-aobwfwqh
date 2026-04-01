class Solution:
    def dfs(self,grid,row,col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
            return 0
        grid[row][col] = 0 #marked as visited
        return 1 + self.dfs(grid,row+1,col) + self.dfs(grid,row-1,col) + self.dfs(grid,row,col+1) + self.dfs(grid,row,col-1) # 1 + becuse we add the value of current node as well so it will either return 0 or give the value of that node
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = self.dfs(grid,row,col)
                    max_area = max(area,max_area)
        return max_area
        
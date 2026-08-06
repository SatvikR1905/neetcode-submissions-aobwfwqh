class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    self.dfs(grid,row,col)
        return count
    def dfs(self,grid,row,col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
            return None

        grid[row][col] = '0'
        self.dfs(grid,row+1,col) # going up
        self.dfs(grid,row-1,col) # going down
        self.dfs(grid,row,col+1) # going right
        self.dfs(grid,row,col-1) # going left


            




        
class Solution:
    def dfs(self,grid,row,col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
            return None # if it reaches end of grid or if it doesnt exist then we return None (edge Case)
        
        grid[row][col] = '0'
        
        self.dfs(grid,row+1,col) #down
        self.dfs(grid,row-1,col) #up
        self.dfs(grid,row,col+1) #right
        self.dfs(grid,row,col-1) #left

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1': # after finding out it is land then increment count
                    count += 1
                    self.dfs(grid,row,col) # call to visit all neighbours
        return count


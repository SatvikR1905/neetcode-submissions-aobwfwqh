class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        minutes = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2: # look for rotten fruit first
                    q.append((row,col))
        while q:
            for i in range(len(q)): #process exactly this minutes rotten fruits
                row , col = q.popleft()

                for (dr,dc) in [[0,1],[1,0],[0,-1],[-1,0]]:
                    r = row + dr
                    c = col + dc

                    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 1:
                        continue # skip everthing you have already found rotten and empty cells

                    grid[r][c] = 2 #fresh fruit becomes rotten also marked as visited
                    q.append((r,c)) # Add newly rotten fruit to queue
            if q: # after processing current level , fresh fruits became rotten at this level
                minutes += 1

        for row in range(len(grid)): #after computation if fresh fruits still exisist then return -1
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        return minutes

        
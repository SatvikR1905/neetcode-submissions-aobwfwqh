class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for rows in range(len(grid)):
            for cols in range(len(grid[0])):
                if grid[rows][cols] == 1:
                    perimeter += 4

                    for (dr,dc) in [(0,1),(0,-1),(1,0),(-1,0)]:
                        r = rows + dr
                        c = cols + dc

                        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                            perimeter -= 1
        return perimeter
        
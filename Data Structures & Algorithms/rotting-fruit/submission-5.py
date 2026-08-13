class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        minutes = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row, col))

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    r = row + dr
                    c = col + dc

                    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 1:
                        continue

                    grid[r][c] = 2
                    q.append((r, c))
            if q:
                minutes += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        return minutes
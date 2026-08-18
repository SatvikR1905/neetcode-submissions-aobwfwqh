class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pac_q = collections.deque()
        atl_q = collections.deque()

        pac = set()
        atl = set()

        for col in range(cols):
            pac_q.append((0,col))
            atl_q.append((rows - 1 , col))

        for row in range(rows):
            pac_q.append((row,0))
            atl_q.append((row,cols - 1))
        
        def bfs(queue,visited):
            while queue:
                row , col = queue.popleft()
                visited.add((row,col))
                for dr , dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    r = row + dr
                    c = col + dc
                    if r < 0 or c < 0 or c >= cols or r >= rows or heights[r][c] < heights[row][col] or (r,c) in visited:
                        continue

                    visited.add((r,c))
                    queue.append((r,c))
        bfs(pac_q,pac)
        bfs(atl_q,atl)

        result = []
        for row in range(rows):
            for col in range(cols):
                if (row,col) in pac and (row,col) in atl:
                    result.append([row,col])

        return result

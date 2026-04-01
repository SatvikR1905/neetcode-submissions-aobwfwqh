class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac_q = collections.deque()
        atl_q = collections.deque()
        pac = set()
        atl = set()

        # Add border cells
        for col in range(cols):
            pac_q.append((0, col))          # top row → pacific
            atl_q.append((rows-1, col))     # bottom row → atlantic

        for row in range(rows):
            pac_q.append((row, 0))          # left col → pacific
            atl_q.append((row, cols-1))     # right col → atlantic

        def bfs(queue, visited):
            while queue:
                row, col = queue.popleft()  # ← pop current cell!
                visited.add((row, col))     # ← mark as visited!
                for (dr,dc) in [(0,1),(0,-1),(1,0),(-1,0)]:
                    r = row + dr
                    c = col + dc
                    if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or heights[r][c] < heights[row][col]:
                        continue
                        
                    visited.add((r,c))
                    queue.append((r,c))

        bfs(pac_q, pac)
        bfs(atl_q, atl)

        result = []
        for row in range(rows):
            for col in range(cols):
                if (row,col) in pac and (row,col) in atl:
                    result.append([row,col])
        return result
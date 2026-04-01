class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = collections.deque()
        rows , cols = len(board) , len(board[0])

        for row in range(rows):
            for col in range(cols):
                if (row == 0 or row == rows - 1 or col == 0 or col == cols-1) and board[row][col] == 'O':
                    q.append((row,col))
        
        while q:
            row , col = q.popleft()
            board[row][col] = 'T'
            for (dr,dc) in [[0,1],[1,0],[0,-1],[-1,0]]:
                r = row + dr
                c = col + dc
                if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                    continue
                board[r][c] = 'T'
                q.append((r,c))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'T':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'
                

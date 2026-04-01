class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list) #creates an empty listfrom 0-8
        cols = defaultdict(list)
        grid = defaultdict(list)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grid[r // 3, c // 3]:
                    return False
                
                cols[c].append(board[r][c])
                rows[r].append(board[r][c])
                grid[r // 3, c // 3].append(board[r][c])
        return True
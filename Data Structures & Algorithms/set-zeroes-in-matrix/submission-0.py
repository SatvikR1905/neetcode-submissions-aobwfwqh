class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for row in zero_rows:
            for j in range(m):
                matrix[row][j] = 0
        for col in zero_cols:
            for i in range(n):
                matrix[i][col] = 0

        

        
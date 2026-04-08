class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j] #transpose of a matrix

        for i in range(n):
            matrix[i].reverse() # reverse in each row

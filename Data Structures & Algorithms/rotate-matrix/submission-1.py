class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n): # we start i greater than i so that we dont swap postions again and again 
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j] #transpose of a matrix

        for i in range(n):
            matrix[i].reverse() # reverse in each row

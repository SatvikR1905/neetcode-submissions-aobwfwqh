class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # perform two binary searches , one is to check which row the target value belongs and the other to check where the number lies inside that particular row itself

        rows = len(matrix)
        cols = len(matrix[0])

        top , bot = 0 , rows - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]: # compare with last digit of the row
                top = row + 1
            elif target < matrix[row][0]: #compae with firdt digit of the row
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False

        l, r = 0, cols - 1
        row = (top + bot) // 2
        while l <= r:
            mid = (l+r) // 2
            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        return False
            

        
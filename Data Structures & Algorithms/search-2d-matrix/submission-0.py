class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        for row in matrix:
            for i in row:
                res.append(i)
        print(res)
        left = 0
        right = len(res) - 1
        while left <= right:
            mid = (left + right) // 2
            if res[mid] == target:
                return True
            elif res[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

        
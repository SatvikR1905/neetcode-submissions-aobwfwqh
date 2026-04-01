class Solution:
    def mySqrt(self, x: int) -> int:
        low , high = 0 , x
        result = 0
        while low <= high:
            mid = (low + high) // 2
            if mid*mid > x:
                high = mid - 1
            else:
                result = mid
                low = mid + 1
        return result
        
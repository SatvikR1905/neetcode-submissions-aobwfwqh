class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        original = n
        while n != 0:
            res = res * x
            if n > 0:
                n -= 1
            else:
                n += 1
        if original > 0:
            return res
        else:
            return 1/res

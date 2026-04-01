class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1

        arr=[]
        for i in range(1,n):
            if i*i <= n:
                arr.append(i*i)

        dp = [float('inf')] * (n+1)

        #Base Case
        dp[0] = 0

        for i in range(1,n+1):
            for num in arr:
                if i - num >= 0:
                    dp[i] = min(dp[i],dp[i-num]+1)
        return dp[n]
        
class Solution:
    def numSquares(self, n: int) -> int:
        arr=[]
        for i in range(1,n+1):
            if i*i <= n:
                arr.append(i*i)

        dp = [float('inf')] * (n+1)
        
        #Base Case
        dp[0] = 0

        for i in range(1,n+1):
            for num in arr:
                if num <= i:
                    dp[i] = min(dp[i], 1 + dp[i-num])
        return dp[n]



        
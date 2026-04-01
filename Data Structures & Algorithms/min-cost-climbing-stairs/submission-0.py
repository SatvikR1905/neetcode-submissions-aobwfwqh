class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # we can reach dp[i] in two ways either taking (i-1) or (i-2) route
        n = len(cost)
        dp = [0] * (n+1)

        #Base cases 
        #There are no cost for starting up from either index 0 or index 1
        dp[0] == 0
        dp[1] == 0

        for i in range(2,n+1): #we need to reach one postion past last index of the array
            dp[i] = min((dp[i-1]+cost[i-1] , dp[i-2]+cost[i-2]))
        return dp[i]
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        #At every step we are trying to rob or skip 
        # skip --> the previous best was dp[i-1]
        #rob --> the previous best was dp[i-2] + nums[i] plus current hidden money 
        n = len(nums)
        dp = [0] * (n)
        #Base Cases
        dp[0] = nums[0] #maximum he can rob if he has single house
        if len(nums) > 1:
            dp[1] = max(nums[0] , nums[1]) # for him now two houses are available so he will take max of both

        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i]) # here we check or make decision that what is suitable to do either to skip or rob the house
        return dp[n-1]
        
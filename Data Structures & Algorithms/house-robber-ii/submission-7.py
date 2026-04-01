class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        
        def max_rob(arr): #helper function
            n = len(arr)
            if n == 1: return arr[0]
            dp = [0] * (n)
            dp[0] = arr[0]
            dp[1] = max(arr[0],arr[1])

            for i in range(2,n):
                dp[i] = max(dp[i-1],dp[i-2]+arr[i])
            return dp[n-1]
        a = max_rob(nums[0:n-1])
        b = max_rob(nums[1:n])
        return max(a,b) 


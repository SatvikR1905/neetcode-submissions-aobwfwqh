class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        dp = [0] * (target + 1)

        #Base Case
        dp[0] = 1

        for i in range(1,target+1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
        return dp[target]




                    
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #intial case when our total is odd we cant split it into equal halves
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        dp = [False] * (target + 1)

        #Base Case
        dp[0] = True

        for num in nums:
            for i in range(target,num-1,-1):
                if dp[i-num] == True:
                    dp[i] = True
        return dp[target]


        
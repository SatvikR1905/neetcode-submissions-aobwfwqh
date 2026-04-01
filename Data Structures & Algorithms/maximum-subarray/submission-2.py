class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        current_sum = 0
        max_sum = -1
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
            elif current_sum < 0:
                current_sum = 0
            else:
                continue
        return max_sum
        

            
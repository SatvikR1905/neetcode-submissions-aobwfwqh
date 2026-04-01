class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n

        #base case starting both max and min of that value is same 
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        for i in range(1,n): # at every position we need to calculate two things whats the max val and min val found till now and at each position we have 3 choices a. to take new number nums[i] or extend previous maximium or extend previous minimum
            dp_max[i] = max(nums[i],dp_max[i-1]*nums[i],dp_min[i-1]*nums[i]) #maximum product of any subarray ending at index i
            dp_min[i] = min(nums[i],dp_max[i-1]*nums[i],dp_min[i-1]*nums[i]) #minimum product of any subarray ending at index i
        return max(dp_max)
        
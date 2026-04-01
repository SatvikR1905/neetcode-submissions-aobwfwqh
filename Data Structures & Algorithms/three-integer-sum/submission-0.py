class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort() # sorting it so that we can perform two sum and have the track of numbers and can remove duplicates
        for i in range(len(nums)):
            if i!=0 and nums[i] == nums[i-1]: #this is to skip duplicates for fixed number and for the first case we dont want to compare first and last element for first iteration
                continue
            l=i+1
            r=len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1 # move left pointer to right for next potential match
                    while l < r and nums[l] == nums[l-1]: # skip duplicates for left pointer
                        l += 1
        return res
                
        
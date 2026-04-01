class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(nums,limit):
            current_sum = 0
            count = 1 # there is atleast one subarray 
            for num in nums:
                if current_sum + num > limit:
                    current_sum = num
                    count += 1
                else:
                    current_sum += num
            return count 

        low , high = max(nums) , sum(nums)
        result = 0
        while low <= high:
            mid = (low+high) // 2
            if cansplit(nums,mid) <= k:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
        
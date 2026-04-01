class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(nums,limit):
            current_sum = 0
            count = 1 # there is atleast one subarray 
            for num in nums:
                if current_sum + num > limit: # we pass the limit as mid value
                    current_sum = num
                    count += 1
                else:
                    current_sum += num
            return count # count how many subarrays we get 

        low , high = max(nums) , sum(nums) # low is when k == n  and high when there is no split and the highest
        result = 0
        while low <= high:
            mid = (low+high) // 2
            if cansplit(nums,mid) <= k: # we found the combination and min of largest we might find better as well right so we save the best result and we go next
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
        
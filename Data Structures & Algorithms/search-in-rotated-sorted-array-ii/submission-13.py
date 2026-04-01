class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[right] == nums[left]: # this is when you arrive at a position where your neighbours are the same and have duplicates EX: [1,0,1,1,1]
                left += 1
                #right -= 1
                continue

            if nums[left] <= nums[mid]: #lies in left portion
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:                       #lies in right portion
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

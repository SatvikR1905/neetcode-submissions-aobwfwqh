class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        cursor = 0
        while cursor <= right:
            if nums[cursor] == 0:
                nums[left] , nums[cursor] = nums[cursor] , nums[left]
                left += 1
                cursor += 1
            elif nums[cursor] == 2:
                nums[right] , nums[cursor] = nums[cursor] , nums[right]
                right -= 1
            else:
                cursor += 1
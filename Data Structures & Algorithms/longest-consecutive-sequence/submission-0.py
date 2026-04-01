class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in num_set: # This condition is to check whether if we are at beginning of the starting sequence
                curr_num = num
                curr_len = 1
                while curr_num + 1 in num_set:
                    curr_len += 1
                    curr_num += 1
                max_len=max(curr_len , max_len)
        return max_len






        
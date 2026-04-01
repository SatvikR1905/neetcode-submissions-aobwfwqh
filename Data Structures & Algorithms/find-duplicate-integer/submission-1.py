class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #treat the array as linkedlist
        fast = 0
        slow = 0
        #phase 1 (we detect where they meet)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        #phase 2 (we try to find the beginning of cycle entrance)
        # Floyd's algorithm where it says the distance from the start to cycle entrance = distance from meeting point to cycle entrance
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow #if they meet thats the entrance of the cycle

        
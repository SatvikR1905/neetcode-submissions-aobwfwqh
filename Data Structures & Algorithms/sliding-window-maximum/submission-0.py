class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # we store indices
        output = []
        l = 0
        r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop() # pop from back of queue
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if(r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output

        
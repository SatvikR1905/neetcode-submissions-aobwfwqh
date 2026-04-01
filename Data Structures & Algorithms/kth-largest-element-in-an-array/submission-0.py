from collections import Counter
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        freq=Counter(nums)
        heap=[]
        #print(freq)
        for num in nums:
            if len(heap) < k or num > heap[0]:
                heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
        
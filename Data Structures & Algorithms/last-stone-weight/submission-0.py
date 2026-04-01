class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap,-s) # negation because we are using max heap

        while len(heap) >= 2: # we need to traverse till we ahave atleast 2 stones in the array
            y = -heapq.heappop(heap) # we need to pop because we either destroy and append  or we keep it as it is , here we cant peep the value
            x = -heapq.heappop(heap)
            if x != y: 
                heapq.heappush(heap,-(y-x)) #this conditions handles all the cases 

        if heap:
            return -heap[0]
        return 0
        
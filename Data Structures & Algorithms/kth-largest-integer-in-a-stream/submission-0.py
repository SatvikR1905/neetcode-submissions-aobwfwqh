
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val) # any value first gets pushed and then we remove the smallest of all
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0] #root will always gives the Kth largest
        

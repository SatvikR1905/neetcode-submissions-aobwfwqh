class MedianFinder:

    def __init__(self):
        self.max_heap = [] # we create max heap to store first set of elements and we want the maximum of that lot
        self.min_heap = [] # we create min_heap to store second set of elements where we want the minimum of that lot so using the average of these two we will return median if the length of total is even
        

    def addNum(self, num: int) -> None:
            heapq.heappush(self.max_heap, -num) # we alwasy push it to max_heap which acts as starting point

            val = -heapq.heappop(self.max_heap) # we move it to min_heap
            heapq.heappush(self.min_heap, val)

            if len(self.min_heap) > len(self.max_heap): #Whatever the current largest number in the left half is, it might actually belong in the right half now that a new number arrived. So let's always send the largest of left half to right half first, then rebalance
                val = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0: # if the total is even we take average of the roots
            return float ((self.min_heap[0] + (-self.max_heap[0])) / 2) # we dont pop we just peek to get value and not remove from the heap entirely
        else:
            return float(-self.max_heap[0]) # if odd we just return root of max_heap
        
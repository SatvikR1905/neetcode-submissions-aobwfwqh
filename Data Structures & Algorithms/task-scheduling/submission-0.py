class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) #we count the frequencies of task and append it to the heap
        heap = [-val for val in count.values()] # this because its o(n) just building thr list 
        heapq.heapify(heap)

        queue = deque() # to process each task one by one
        time = 0
        while queue or heap:
            time += 1

            if heap:
                freq = heapq.heappop(heap)
                freq += 1 # we negate right so we need to add + 1
                if freq != 0:
                    queue.append((time+n,freq))
            else:
                time = queue[0][0] # if the heap is empty we directly move to the time available in first of the queue instead of wating iterations

            if queue and queue[0][0] <= time:
                heapq.heappush(heap,queue.popleft()[1]) #popleft() is a function call and we move only the frequency into the heap and not the time so 1
        return time
            
            


        
        
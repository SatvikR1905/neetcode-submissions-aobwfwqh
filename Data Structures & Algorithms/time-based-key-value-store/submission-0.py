from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) #creates deafult value list for the key
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp , value)) #stores the associated value and timestamp for that particular key
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key] #Store the associate value and timestamp for that particular key into array
        left = 0
        right = len(arr) - 1
        best = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                best = mid
                left = mid + 1 #There might be a better timestamp on the right side
            else:
                right = mid - 1
        return "" if best == -1 else arr[best][1]
        

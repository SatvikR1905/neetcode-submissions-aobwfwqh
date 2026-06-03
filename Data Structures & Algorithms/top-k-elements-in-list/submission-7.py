class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        for num in nums:
            if num in frequent:
                frequent[num] += 1
            else:
                frequent[num] = 1
        arr = []
        for num, val in frequent.items(): #.items used for displaying the key value pairs in a list
            arr.append([val,num])
        arr.sort()
        

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        

            

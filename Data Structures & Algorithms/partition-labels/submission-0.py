class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        last = {}
        for i , char in enumerate(s):
            last[char] = i

        start = 0
        end = 0
        for i , char in enumerate(s):
            end = max(end,last[char])
            if i == end:
                size = end - start + 1
                result.append(size)
                start = i + 1
        return result
            

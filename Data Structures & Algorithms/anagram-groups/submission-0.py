class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for s in strs:
            count = [0] * 26 #intializing all the characters to 0
            for c in s:
                count[ord(c) - ord("a")] += 1 #counting the occurance of characters

            res[tuple(count)].append(s) #keys should always immutable

        return res.values() #returning the values
        

        
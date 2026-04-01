class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            res += str(len(s)) + "#" + s # here we are encoding the string of strings into one string seperated by the length of that string with additional delimiter to separate the strings
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i = 0
        while i < len(s):
            j = i #pointer to track the delimiter
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res

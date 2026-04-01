class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 # start of our window where it starts
        hashmap = {} # memory lookup to see where character's last seen index
        max_length = 0

        for right in range(len(s)):
            char = s[right]
            if char in hashmap and hashmap[char] >= left:
                left = hashmap[char] + 1
            hashmap[char] = right
            max_length = max(max_length , (right - left) + 1)
        return max_length
        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hashmap = {}
        max_length = 0
        for right in range(len(s)):
            char = s[right]
            if char in hashmap: # we have hashmap to track the occurance of the character 
                hashmap[char] += 1
            else:
                hashmap[char] = 1
            window_size = (right - left) + 1
            if window_size - max(hashmap.values()) <= k: #number of replacements = window - size - maximum ocuurances of a character its valid only if its less than or equal to k
                max_length = max(max_length,window_size) # uf yes then we update the max_length
            else:
                hashmap[s[left]] -= 1 #if the condition is invalid we move the left pointer to next and also remove the occurance of that character in hashmap
                left += 1
        return max_length
        
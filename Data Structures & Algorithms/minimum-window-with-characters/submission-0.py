class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="" : # edge Case
            return ""

        t_hashmap = {}
        for char in t: # creating hashmap for counting the frequency of the t string
            t_hashmap[char] = t_hashmap.get(char, 0) + 1 # if it doesnt exist add to the hashmap if it already exists then increase the frequency
        
        w_hashmap = {}
        # validity Check
        have = 0 #number of UNIQUE characters satisfied so far
        need = len(t_hashmap) #number of UNIQUE characters required

        result = ""
        result_len = float("infinity")

        left = 0
        for right in range(len(s)):
            char = s[right]
            w_hashmap[char] = w_hashmap.get(char, 0) + 1

            if char in t_hashmap and w_hashmap[char] == t_hashmap[char]:
                have += 1

            while have == need: # we got a valid window
                if (right - left + 1) < result_len:
                    result_len = right - left + 1
                    result = s[left:right+1] #we join the valid substring which we got 
                w_hashmap[s[left]] -= 1 # start shrinking the left
                if s[left] in t_hashmap and w_hashmap[s[left]] < t_hashmap[s[left]]: # if the left element is present in the t_hashamp and if the frequency of that character present in the current window is below the actual requirement of that character then the window is invalid
                    have -= 1
                left += 1
        return result

        


        
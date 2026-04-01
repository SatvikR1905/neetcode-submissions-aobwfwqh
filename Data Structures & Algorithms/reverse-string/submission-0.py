class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            if s[left] != s[right]:
                print(s[left],s[right])
                s[left],s[right] = s[right],s[left]
                print(s[left],s[right])
            left += 1
            right -= 1
            
                


        
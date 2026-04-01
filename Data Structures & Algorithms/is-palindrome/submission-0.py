class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        result=[]
        for char in lower:
            if char.isalnum():
                result.append(char)
        
        if result == result[::-1]:
            return True
        else:
            return False


        
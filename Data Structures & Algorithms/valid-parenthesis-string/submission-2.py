class Solution:
    def checkValidString(self, s: str) -> bool:
        max_open = 0
        min_open = 0
        
        for char in s:
            if char == "(":
                max_open += 1
                min_open += 1
            elif char == ")":
                max_open -= 1
                min_open -= 1
            else:
                max_open += 1
                min_open -= 1

            if min_open < 0:
                min_open = 0

            if max_open < 0:
                return False

        if min_open == 0:
            return True
        else:
            return False  
        
        
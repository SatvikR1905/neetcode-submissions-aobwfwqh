class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']': # we find any character other than the closing bracket we push it 
                stack.append(char)
            else:
                current_string = ""
                while stack[-1] != '[': # we pop till we find the intial openigng bracket and collect it in string
                    current_string += stack.pop()
                current_string = current_string[::-1] # we reverse it

                stack.pop() # we pop the opening bracket

                num = ""
                while stack and stack[-1].isdigit(): # we collect num in string 
                    num += stack.pop() 
                num = int(num[::-1]) #reverse it 

                for c in current_string * num:
                    stack.append(c) #and then append back that many times back to stack 
        return ''.join(stack) #finally return as a string

        
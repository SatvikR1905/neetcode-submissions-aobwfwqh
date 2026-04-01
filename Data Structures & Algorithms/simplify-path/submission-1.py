class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        clean = path.split('/')
        for str in clean:
            if str not in ['.','','..']:
                stack.append(str)
            elif str == '..' and stack:
                stack.pop()
        return '/' + '/'.join(stack) # '/' we add in the beginning and the other we concatenate everything with '/'

     

        
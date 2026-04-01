class MinStack:

    def __init__(self): #special contructor method which is itialized automatically when object is created
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack: # if stack is empty it appends the value 
            self.minStack.append(val)
        else:
            self.minStack.append(min(val,self.minStack[-1])) # if it exisists then compares the min value and then append

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop() #Should pop in sync
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        

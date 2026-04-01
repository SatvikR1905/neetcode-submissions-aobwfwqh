class MyQueue:

    def __init__(self):
        self.stack_back = []
        self.stack_front = []

    def push(self, x: int) -> None:
        self.stack_back.append(x)

    def pop(self) -> int:
        if not self.stack_front:
            while self.stack_back:
                self.stack_front.append(self.stack_back.pop())
        return self.stack_front.pop()

    def peek(self) -> int:
        if not self.stack_front:
            while self.stack_back:
                self.stack_front.append(self.stack_back.pop())
        return self.stack_front[-1]

    def empty(self) -> bool:
        return not self.stack_back and not self.stack_front
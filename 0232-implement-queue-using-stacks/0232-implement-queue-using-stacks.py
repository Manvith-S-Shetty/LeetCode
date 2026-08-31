class MyQueue:
    
    def __init__(self):
        self.inputst=[]
        self.outputst = []

    def push(self, x: int) -> None:
        self.inputst.append(x)

    def pop(self) -> int:
        self.move()
        return self.outputst.pop()

    def peek(self) -> int:
        self.move()
        return self.outputst[-1]

    def empty(self) -> bool:
        return not self.inputst and not self.outputst

    def move(self):
        if not self.outputst:
            while self.inputst:
                self.outputst.append(self.inputst.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
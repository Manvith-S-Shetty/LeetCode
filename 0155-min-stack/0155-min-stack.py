class MinStack:

    def __init__(self):
        self.st = []
        self.mins = []

    def push(self, value: int) -> None:
        self.st.append(value)
        if not self.mins:
            self.mins.append(value)
        else:
            
            self.mins.append(min(value,self.mins[-1]))
            

    def pop(self) -> None:
        self.st.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
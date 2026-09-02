class CustomStack:

    def __init__(self, maxSize: int):
        self.st = []
        self.maxSize = maxSize
        self.inc = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.st) < self.maxSize:
            self.st.append(x)

    def pop(self) -> int:
        # Check if stack is empty first
        if not self.st:
            return -1

        # 1. Get the current top index safely using length
        id = len(self.st) - 1
        
        # 2. Pop ONLY ONCE and add the lazy increment value
        res = self.st.pop() + self.inc[id]

        # 3. Pass the lazy increment down to the next lower element
        if id > 0:
            self.inc[id - 1] += self.inc[id]
            
        # 4. Clear the current index tracker and return the value
        self.inc[id] = 0
        return res

    def increment(self, k: int, val: int) -> None:
        # Correctly calculate the targeted bottom index boundary
        id = min(k, len(self.st)) - 1
        if id >= 0:
            self.inc[id] += val

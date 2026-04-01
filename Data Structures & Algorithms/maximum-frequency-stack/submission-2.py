class FreqStack:

    def __init__(self):
        self.count = {}
        self.maxCount = 0
        self.stacks = {} 

    def push(self, val: int) -> None:
        valCount = 1 + self.count.get(val, 0)
        self.count[val] = valCount
        if valCount > self.maxCount:
            self.maxCount = valCount
            self.stacks[valCount] = []
        self.stacks[valCount].append(val)

    def pop(self) -> int:
        sol = self.stacks[self.maxCount].pop()
        self.count[sol] -= 1
        if not self.stacks[self.maxCount]:
            self.maxCount -= 1
        return sol


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
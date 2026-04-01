class FreqStack:

    def __init__(self):
        self.stack = []
        self.counts = {}

    def push(self, val: int) -> None:
        self.counts[val] = self.counts.get(val, 0) + 1
        self.stack.append(val)

    def pop(self) -> int:
        maxCnt = max(self.counts.values())
        i = len(self.stack) - 1
        while self.counts[self.stack[i]] != maxCnt:
            i -= 1
        self.counts[self.stack[i]] -= 1
        return self.stack.pop(i)

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
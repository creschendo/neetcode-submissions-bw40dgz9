class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        print(self.s1)
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        print(self.s1)
        while self.s2:
            self.s1.append(self.s2.pop())
        print(self.s1)

    def pop(self) -> int:
        return self.s1.pop()
        
    def peek(self) -> int:
        return self.s1[-1]
        
    def empty(self) -> bool:
        if self.s1:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
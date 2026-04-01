class FreqStack:

    def __init__(self):
        # count occurences of all elements
        self.count = {}

        # track highest occurences
        self.maxCount = 0

        # keep dict of stacks for each count
        self.stacks = {} 

    def push(self, val: int) -> None:
        # count the number of occurences for new element
        valCount = 1 + self.count.get(val, 0)

        # set count
        self.count[val] = valCount

        # check if new max count is found
        if valCount > self.maxCount:

            # set new max
            self.maxCount = valCount

            # create new stack for max count
            self.stacks[valCount] = []

        # add to end of count stack
        self.stacks[valCount].append(val)

    def pop(self) -> int:

        # the most recently pushed in highest count stack is solution
        sol = self.stacks[self.maxCount].pop()

        # subtract count
        self.count[sol] -= 1

        # if no more elements in maxcount stack, decrement max
        if not self.stacks[self.maxCount]:
            self.maxCount -= 1
        
        return sol


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
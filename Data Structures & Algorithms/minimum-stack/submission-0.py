class MinStack:

    def __init__(self):
        # base stack
        self.stack = []

        # stack that keeps track of the min at each index
        self.minstack = []

    def push(self, val: int) -> None:
        # standard stack push
        self.stack.append(val)

        # calculating the min at the new index
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(self.minstack[-1], val))

    def pop(self) -> None:
        # pop from stack
        self.stack.pop()

        # pop from minstack
        self.minstack.pop()

    def top(self) -> int:
        # return top of the stack
        # not necessarily the min
        return self.stack[-1]

    def getMin(self) -> int:
        # return the top of the minstack, which represents the min at
        # that index, which happens to be the global min
        return self.minstack[-1]

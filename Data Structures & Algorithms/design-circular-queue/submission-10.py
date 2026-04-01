class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        # create ring of list nodes
        self.front = self.rear = ListNode(-1, None)

        # add k - 1 more nodes to ring
        for _ in range(k - 1):
            self.rear.next = ListNode(-1, None)
            self.rear = self.rear.next

        # connect the last node to the first
        self.rear.next = self.front

        # empty queue, rear = front
        self.rear = self.front

    def enQueue(self, value: int) -> bool:
        # full queue case
        if self.rear.next == self.front and self.k != 1:
            return False

        # empty queue case
        elif self.rear == self.front and self.rear.val == -1:
            self.rear.val = value
            return True
        
        # general case
        else:
            self.rear.next.val = value
            self.rear = self.rear.next
            return True

    def deQueue(self) -> bool:
        # empty case
        if self.front.val == -1:
            return False

        # general and full case
        else:
            self.front.val = -1
            if self.front != self.rear:
                self.front = self.front.next
            return True

    def Front(self) -> int:
        # empty case
        if self.front.val == -1:
            return -1

        # general case
        else:
            return self.front.val
        

    def Rear(self) -> int:
        # empty case
        if self.rear.val == -1:
            return -1

        # general case
        else:
            return self.rear.val

    def isEmpty(self) -> bool:
        return self.front.val == -1
        

    def isFull(self) -> bool:
        return self.rear.next == self.front
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
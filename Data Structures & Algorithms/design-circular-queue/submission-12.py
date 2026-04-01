class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class MyCircularQueue:
    def __init__(self, k: int):
        # set size and capacity
        self.size = 0
        self.k = k

        # create ring
        self.front = ListNode()
        cur = self.front
        for _ in range(k - 1):
            cur.next = ListNode()
            cur = cur.next

        # connect last node to first
        cur.next = self.front

        # both start at same node
        self.rear = self.front 

    def enQueue(self, value: int) -> bool:
        # full case
        if self.isFull():
            return False

        # empty case
        if self.isEmpty():
            self.rear.val = value

        # general case
        else:
            self.rear = self.rear.next
            self.rear.val = value
        
        self.size += 1
        return True

    def deQueue(self) -> bool:
        # empty case
        if self.isEmpty():
            return False
        
        # general case
        self.front = self.front.next
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.front.val
        

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.rear.val

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
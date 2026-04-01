class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        if not self.left or num < abs(self.left[0]):
            heapq.heappush(self.left, -1 * num)
        else:
            heapq.heappush(self.right, num)
        self.balance()
        
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0] * -1
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return ((self.left[0] * -1) + self.right[0]) / 2

    def balance(self):
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -1 * heapq.heappop(self.left))
        elif len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left, -1 * heapq.heappop(self.right))
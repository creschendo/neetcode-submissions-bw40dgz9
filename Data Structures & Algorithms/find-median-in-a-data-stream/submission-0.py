class MedianFinder:
    import bisect
    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.bisect.insort(self.data, num)

    def findMedian(self) -> float:
        if len(self.data) % 2 == 1:
            return float(self.data[len(self.data)//2])
        pos = len(self.data) // 2
        val = self.data[pos - 1] + self.data[pos]
        return float(val / 2)
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
            return self.minHeap[0]
        elif val < self.minHeap[0]:
            return self.minHeap[0]
        else:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)
            return self.minHeap[0]


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)

        # keep only k elements in a min heap
        # the top element will always be the kth largest
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # haven't reached k elements yet, just add and return the smallest
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
            return self.minHeap[0]
        # heap is full and value is smaller than smallest, 
        # just return the smallest 
        elif val < self.minHeap[0]:
            return self.minHeap[0]
        # heap is full and new value isn't the smallest, 
        # pop the smallest, add the new value, and return the
        # new smallest
        else:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)
            return self.minHeap[0]


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)
        for stone in stones:
            heapq.heappush(maxHeap, (-1) * stone)
        
        while len(maxHeap) > 1:
            stone1 = (-1) * heapq.heappop(maxHeap)
            stone2 = (-1) * heapq.heappop(maxHeap)  
            if stone1 != stone2:
                heapq.heappush(maxHeap, (-1) * abs(stone1-stone2))
        
        return (-1) * maxHeap[-1] if maxHeap else 0
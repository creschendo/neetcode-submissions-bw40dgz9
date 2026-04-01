class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            maxHeap.append(-1 * stone)
        
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)
            diff = abs(stone1 - stone2)
            if diff:
                heapq.heappush(maxHeap, -1 * diff)
        
        return (-1 * maxHeap[0]) if maxHeap else 0

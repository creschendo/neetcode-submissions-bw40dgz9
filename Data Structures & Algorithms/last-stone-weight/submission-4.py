class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [x  * -1 for x in stones]
        print(heap)
        heapq.heapify(heap)

        while len(heap) > 1:
            s1, s2 = heapq.heappop(heap), heapq.heappop(heap)
            print(s1)
            print(s2)
            diff = abs(s1 - s2)
            if diff:
                heapq.heappush(heap, -1 * diff)
        
        return heap[0] * -1 if heap else 0

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)
        for point in points:
            x, y = point[0], point[1]
            dist = (x * x) + (y * y)
            heapq.heappush(maxHeap, (-1 * dist, x, y))
                
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [(x, y) for _, x, y in maxHeap]
        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x, y = point[0], point[1]
            dist =  (x**2) + (y**2)
            heapq.heappush(heap, (-1 * dist, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)

        return [point for _, point in heap]

        

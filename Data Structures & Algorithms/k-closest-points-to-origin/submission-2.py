import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)

        for point in points:
            dist = math.sqrt((point[0] ** 2) + (point[1] ** 2))

            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-1 * dist, point))
            elif (-1) * dist > maxHeap[0][0]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (-1 * dist, point))
        return [(point) for _, point in maxHeap]
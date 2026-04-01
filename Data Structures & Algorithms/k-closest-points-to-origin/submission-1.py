class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)
        # maintain a size k max heap that keeps track of the k
        # smallest distances
        for point in points:
            x, y = point[0], point[1]

            # no need to square root if we don't return distance
            dist = (x * x) + (y * y)

            # push to maxHeap
            heapq.heappush(maxHeap, (-1 * dist, x, y))
            
            # remove if size too big
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        # return points
        return [(x, y) for _, x, y in maxHeap]
        
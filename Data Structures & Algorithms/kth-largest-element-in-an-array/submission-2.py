class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            elif num > minHeap[0]:
                heapq.heappush(minHeap, num)
                heapq.heappop(minHeap)
        
        return minHeap[0]

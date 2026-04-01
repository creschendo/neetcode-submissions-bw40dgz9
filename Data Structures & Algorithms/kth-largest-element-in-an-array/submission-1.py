class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        # maintain k-sized minHeap
        # top will be the kth largest

        for num in nums:
            # push to minHeap
            heapq.heappush(minHeap, num)

            # if size exceeds k, pop the smallest, which
            # keeps the k largest numbers
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]
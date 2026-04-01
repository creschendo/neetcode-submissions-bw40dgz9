class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        stops = sorted(trips, key = lambda x: x[1])

        print(stops)
        people = 0
        minHeap = []

        for ppl, start, end in stops:
            people += ppl

            while minHeap and start >= minHeap[0][0]:
                people -= minHeap[0][1]
                heapq.heappop(minHeap)
            
            if people > capacity:
                return False
            
            heapq.heappush(minHeap, (end, people))
        return True





class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # sort stops by start ascending
        stops = sorted(trips, key = lambda x: x[1])

        # current passenger count
        people = 0

        # stores people still in the car, top is next drop off
        minHeap = []

        for ppl, start, end in stops:
            # add new people
            people += ppl

            # remove all dropped off people
            while minHeap and start >= minHeap[0][0]:
                people -= heapq.heappop(minHeap)[1]
            
            # check capacity
            if people > capacity:
                return False
            
            # add current trip to heap
            heapq.heappush(minHeap, (end, people))

        # reach end without exceeding, good
        return True





class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort all trips by start location
        trips.sort(key=lambda t: t[1])

        # use a minHeap to track passengers 
        # currently in the car, and num people
        minHeap = []
        curPass = 0


        for numPass, start, end in trips:
            # remove every passenger for which we've dropped off
            # at this point or prior to this point
            while minHeap and minHeap[0][0] <= start:
                curPass -= heapq.heappop(minHeap)[1]

            # add the current passengers getting on
            curPass += numPass

            # if more than capacity, impossible
            if curPass > capacity:
                return False
            
            # add the current passengers 
            heapq.heappush(minHeap, [end, numPass])
        
        return True
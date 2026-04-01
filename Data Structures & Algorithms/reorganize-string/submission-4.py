class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)

        heap = [] 
        for char, count in counts.items():
            heapq.heappush(heap, (-1 * count, char))
        

        sol = []
        prev = None

        while heap:
            # retrieve max count element
            count, char = heap[0]

            # pop from heap
            if heap:
                heapq.heappop(heap)

            # add to solution
            sol.append(char)

            # subtract from character count
            count += 1

            # push previous letter
            if prev:
                heapq.heappush(heap, prev)

            # update prev if current still has count
            if count:
                prev = (count, char)
            else:
                prev = None
        
        if prev:
            return ""
        
        return "".join(sol)
            

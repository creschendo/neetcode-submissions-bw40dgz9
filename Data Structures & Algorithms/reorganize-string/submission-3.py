import math
class Solution:
    def reorganizeString(self, s: str) -> str:
        # count all frequencies 
        count = Counter(s)

        # create a maxHeap with all negative counts and characters
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        # previous stores the last appended character
        prev = None
        sol = ""

        while maxHeap or prev:
            # prev and no maxHeap means a duplicate is inevitable
            if prev and not maxHeap:
                return ""

            # pop character with highest count
            cnt, char = heapq.heappop(maxHeap)

            # append to solution
            sol += char
            cnt += 1

            # push the prior character back to the maxHeap
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None 
            
            # set new previous to current character, if more left
            # dont repush to avoid duplicates
            if cnt != 0:
                prev = [cnt, char]

        return sol



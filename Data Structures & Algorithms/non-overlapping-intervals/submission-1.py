class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # First sort the intervals on start value
        sortedints = sorted(intervals, key = lambda x: x[0])

        end = sortedints[0][1]
        sol = 0

        for inter in sortedints[1:]:
            if inter[0] >= end:
                end = inter[1]
            else:
                end = min(end, inter[1])
                sol += 1
        
        return sol
        

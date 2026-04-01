class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # First sort the intervals on start value
        sortedints = sorted(intervals, key = lambda x: x[0])

        # Set the first right bound
        end = sortedints[0][1]

        # Set count
        sol = 0

        # Iterate through the rest of the sorted intervals
        for inter in sortedints[1:]:

            # If the interval doesn't overlap with prev, 
            # update right bound to the current interval
            if inter[0] >= end:
                end = inter[1]

            # If it does overlap, eliminate the interval
            # with the higher right bound to minimize deletions
            # greedily and add to deletion count
            else:
                end = min(end, inter[1])
                sol += 1
        

        return sol
        

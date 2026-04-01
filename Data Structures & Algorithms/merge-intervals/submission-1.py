class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort all intervals by starting value
        sortedints = sorted(intervals, key = lambda x: x[0])

        # Initialize solution to first interval in sorted set
        sol = [sortedints[0]]
        
        # Iterate through all other sorted intervals
        for interval in sortedints[1:]:

            # Overlap, merge the last inserted and the new interval
            if interval[0] <= sol[-1][1]:
                newInterval = [
                    min(sol[-1][0], interval[0]), 
                    max(sol[-1][1], interval[1])
                ]
                sol[-1] = newInterval
            
            # No overlap, just append the next interval
            else:
                sol.append(interval)
        
        # Return solution
        return sol
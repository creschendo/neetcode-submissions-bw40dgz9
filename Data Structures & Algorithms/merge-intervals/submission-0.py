class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedints = sorted(intervals, key = lambda x: x[0])
        sol = [sortedints[0]]
        
        for interval in sortedints[1:]:
            if interval[0] <= sol[-1][1]:
                newInterval = [
                    min(sol[-1][0], interval[0]), 
                    max(sol[-1][1], interval[1])
                ]
                sol[-1] = newInterval
            else:
                sol.append(interval)
        
        return sol
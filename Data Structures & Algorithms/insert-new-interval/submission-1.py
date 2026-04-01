class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        sol = []
        
        for i in range(len(intervals)):
            # Insert new interval
            if newInterval[1] < intervals[i][0]:
                sol.append(newInterval)
                return sol + intervals[i:]
            
            # Insert existing interval
            elif newInterval[0] > intervals[i][1]:
                sol.append(intervals[i])
            
            # Overlap, continuously update new and insert later
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])
                ]
        # If new interval wasn't inserted yet
        sol.append(newInterval)
        return sol
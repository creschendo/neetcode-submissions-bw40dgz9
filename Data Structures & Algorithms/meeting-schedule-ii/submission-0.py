"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # check for empty list
        if not intervals:
            return 0
        
        start = []
        end = []

        for inter in intervals:
            start.append(inter.start)
            end.append(inter.end)
        
        start.sort()
        end.sort()

        sol = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            sol = max(sol, count)
        
        return sol

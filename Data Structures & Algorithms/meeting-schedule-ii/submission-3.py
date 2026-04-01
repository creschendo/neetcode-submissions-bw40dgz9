"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Greedy Approach
        times = []
        for inter in intervals:
            times.append((inter.start, 1))
            times.append((inter.end, -1))

        times.sort(key=lambda x: (x[0], x[1]))

        sol = count = 0
        for time in times:
            count += time[1]
            sol = max(sol, count)

        return sol
        # Two Pointers approach
        """
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

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
        """
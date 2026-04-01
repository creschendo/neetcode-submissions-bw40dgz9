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

        # add all start times with a +1
        # add all end times with a -1
        times = []
        for inter in intervals:
            times.append((inter.start, 1))
            times.append((inter.end, -1))

        # sort by start time first, and if same, sort by end
        # makes sure that meeting ends will be counted first and correctly
        times.sort(key=lambda x: (x[0], x[1]))

        # iterate through all times
        # every start, add 1
        # every end, subtract 1
        # the max concurrent meetings is the minimum number of rooms
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
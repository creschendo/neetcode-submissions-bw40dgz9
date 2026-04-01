"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # check for empty list
        if not intervals:
            return True
        
        # sort by start time
        sortedints = sorted(intervals, key = lambda x: x.start)
        end = sortedints[0].end

        # check for overlaps
        for inter in sortedints[1:]:
            if inter.start < end:
                return False
            end = inter.end
        
        return True
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

#basically the min num of buckets/days where in any given day there is no overlap

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # start and end times will be able to tell us the number of meetings rooms at a given T

        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])


        res,count = 0,0
        s=e=0

        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                s+=1
            else:
                count -= 1
                e += 1
            res = max(res,count)
        
        return res
        
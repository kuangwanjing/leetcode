# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key = lambda x: x.start)
        rooms = [[] for i in intervals]
        #print (rooms)
        count = 0
        for i, inter in enumerate(intervals):
            for j in range(0, len(rooms)):
                if not rooms[j]: count += 1
                if not rooms[j] or intervals[rooms[j][-1]].end <= inter.start: 
                    rooms[j].append(i)
                    break  
        return count

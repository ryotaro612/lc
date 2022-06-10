
"""
d = [0] * 22
d[0] += 1
d[31] = -1
d[5] += 1
d[11] -= 1
d[15] += 1
d[21] -= 1

d[1] += d[0]
d[2] += d[1]

[[13,15],[1,13]]
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        for i in range(n-1):
            if intervals[i+1][0] < intervals[i][1]:
                return False
        return True    

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

0 1 2  3  4 5  6 7 8 9 10
0 1 -1      1 -1
  2    -1
0 2 -1 -1 1 1 -1 0 0 0 -1
0 2 1  0  1 2  1 1 1 1 0
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        times = set()
        for intervals in schedule:
            for interval in intervals:
                times.add(interval.start)
                times.add(interval.end)
        timemap, rev_timemap = dict(), dict()
        count = 0
        times = sorted(list(times))
        for time in times:
            timemap[time] = count
            rev_timemap[count] = time
            count += 1
            
        prefix = [0] * (timemap[times[-1]] + 1)
        
        for intervals in schedule:
            for interval in intervals:
                prefix[timemap[interval.start]] += 1
                prefix[timemap[interval.end]] -= 1
        
        n = len(prefix)
        for i in range(1, n):
            prefix[i] += prefix[i-1]
        # print(prefix)
        free = []
        start, end = -1, -1
        for i in range(n):
            if i > 0 and prefix[i] == 0 and prefix[i-1] > 0:
                start = i
            if i > 0 and prefix[i] > 0 and prefix[i-1] == 0:
                end = i
                # print(start, end)
                free.append(Interval(rev_timemap[start], rev_timemap[end]))
        return free
    


"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

0 1 2  3  4 5  6 7 8 9 10
0 1 -1      1 -1
  2    -1
0 2 -1 -1 1 1 -1 0 0 0 -1
0 2 1  0  1 2  1 1 1 1 0
"""

class Solution2:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        timeline = []
        for intervals in schedule:
            for interval in intervals:
                timeline.append(interval)
                
        timeline.sort(key=lambda interval: interval.start)
        n = len(timeline)
        result = []
        
        cur = timeline[0]
        for i in range(1, n):
            if cur.end < timeline[i].start:
                result.append(Interval(cur.end, timeline[i].start))
            if cur.end < timeline[i].end:
                cur = timeline[i]
        return result
            

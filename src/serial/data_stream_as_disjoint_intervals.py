from collections import deque

class SummaryRanges:

    def __init__(self):
        self.intervals = []        
        self.added = []
    def addNum(self, value: int) -> None:
        self.added.append(value)

    def getIntervals(self) -> List[List[int]]:
        vals = sorted(self.added)
        i = 0
        n = len(vals)
        self.added = []
        result = []
        
        for start, end in self.intervals:
            while i < n and vals[i] < start:
                if result and vals[i] <= result[-1][1] + 1:
                    result[-1][1] = max(result[-1][1], vals[i])
                else:
                    result.append([vals[i], vals[i]])
                i+=1

            while i < n and vals[i] <= end:
                i += 1
                
            if result and start <= result[-1][1] + 1:
                result[-1][1] = end
            else:
                result.append([start, end])
        
        while i < n:
            if result and vals[i] <= result[-1][1] + 1:
                result[-1][1] = max(result[-1][1], vals[i])
            else:
                result.append([vals[i], vals[i]])
            i += 1

        self.intervals = result
        return result


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()

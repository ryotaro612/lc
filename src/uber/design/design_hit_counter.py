import bisect

class HitCounter:

    def __init__(self):
        self.history = []        

    def hit(self, timestamp: int) -> None:
        if len(self.history) > 0 and self.history[-1][0] == timestamp:
            self.history[-1] = (self.history[-1][0], self.history[-1][1] + 1)
        else:
            self.history.append((timestamp, 1))

    def getHits(self, timestamp: int) -> int:
        """(timestamp-300, timestamp]"""
        lb, ub = -1, len(self.history)
        while ub - lb > 1:
            mid = (ub + lb) // 2
            if self.history[mid][0] <= timestamp - 300:
                lb = mid
            else:
                ub = mid
        
        index = ub       
        n = len(self.history)
        result = 0
        # print(timestamp, index, self.history)
        while index < n and self.history[index][0] <= timestamp:
            result += self.history[index][1]
            index += 1
        return result

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

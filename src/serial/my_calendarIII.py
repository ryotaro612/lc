class MyCalendarThree:

    def __init__(self):
        self.times = set() 
        self.events = []
    def book(self, startTime: int, endTime: int) -> int:
        self.events.append([startTime, endTime])
        self.times.add(startTime)
        self.times.add(endTime)
        remap = dict()
        i = 0
        for j in sorted(self.times):
            remap[j] = i
            i += 2

        distances = [0] * (i+1)
        for [s, e] in self.events:
            distances[remap[s]+1] += 1
            distances[remap[e]] -= 1
        
        for i in range(1, len(distances)):
            distances[i] += distances[i-1]
        res = 0

        for i in range(len(distances)):
            res = max(res, distances[i])
        
        return res

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)

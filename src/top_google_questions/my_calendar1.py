"""
["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
[[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
"""
import bisect

class MyCalendar:

    def __init__(self):
        self.schedule = []

    def book(self, start: int, end: int) -> bool:
        if not self.schedule:
            self.schedule.append([start, end])
            return True
        
        inserted = False
        n = len(self.schedule)
        next_schedule = []
        for i, event in enumerate(self.schedule):
            if inserted:
                next_schedule.append(event)
            elif (i == 0 or self.schedule[i-1][1] <= start) and end <= event[0]:
                next_schedule.append([start, end])
                next_schedule.append(event)
                inserted = True
            else:
                next_schedule.append(event)
        if inserted:
            self.schedule = next_schedule
            return True 
        elif self.schedule[-1][1] <= start:
            self.schedule = next_schedule
            self.schedule.append([start, end])
            return True
        else:
            return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

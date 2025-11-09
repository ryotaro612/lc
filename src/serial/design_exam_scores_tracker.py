from bisect import bisect_right, bisect_left

class ExamTracker:

    def __init__(self):
        """
        score[0], score[1]
        prefix[i] = sum(score[:i])
        prefix[i] = sum[i-1] + prefix[i-1]
        prefix[i] - prefix[j] = sum[j:i]
        """
        self.prefix = []
        self.time = []

    def record(self, time: int, score: int) -> None:
        if self.prefix == []:
            self.prefix.append(score)
        else:
            self.prefix.append(score + self.prefix[-1])

        self.time.append(time)

    def totalScore(self, startTime: int, endTime: int) -> int:
        l = bisect_left(self.time, startTime)
        r = bisect_right(self.time, endTime)

        if r == 0:
            return 0
        if l == 0:
            if self.time[0] < startTime:
                return self.prefix[r-1] - self.prefix[0]
            else:
                return self.prefix[r-1]
        return self.prefix[r-1] - self.prefix[l-1]



# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)

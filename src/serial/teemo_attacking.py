class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0:
            return 0
        n = len(timeSeries)
        result = 0
        for i, time in enumerate(timeSeries):
            if i == n-1:
                return result + duration
            else:
                result += min(duration, timeSeries[i+1] - time)

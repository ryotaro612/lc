class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])

        counter = 0
        edge = -float("inf")
        for left, right in intervals:
            if edge <= left:
                counter += 1
                edge = right

        return len(intervals) - counter

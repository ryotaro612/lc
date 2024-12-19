import bisect

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        # print(intervals)
        result = []
        for start, end in intervals:
            # print(result)
            i = bisect.bisect_left(result, start)
            if i == len(result):
                result.extend([end-1, end])
                continue
            if result[i] <= end:
                if i < len(result) - 1 and result[i+1] <= end:
                    continue
                else:
                    if end == result[-1]:
                        result.pop()
                        result.extend([end-1, end])
                    else:
                        result.append(end)
        
        return len(result)

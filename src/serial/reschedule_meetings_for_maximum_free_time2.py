class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        """
        duration[i] end[i] - start[i]
        start[i+1] - end[i-1] - duration[i]
        
        (duration, start[i], end[i])
        """
        n = len(startTime)
        for i in range(n):
            duration = endTime[i] - startTime[i]
            if i == 0:
                result = startTime[1] - duration
                continue
            if i == n - 1:
                result = max(result, eventTime - endTime[n-2] - duration)
                continue
            
            result = max(result, startTime[i+1] - endTime[i-1] - duration)
        

        durations = []
        for i in range(n):
            if i == 0:
                durations.append([startTime[0], 0])
                continue
            durations.append([startTime[i]-endTime[i-1], i])
            if i == n - 1:
                durations.append([eventTime-endTime[n-1], i+1])
        
        durations.sort(reverse=True)

        for i in range(n):
            span = endTime[i] - startTime[i]
            for j in range(3):
                if span <= durations[j][0] and i != durations[j][1] and i + 1 != durations[j][1]:
                    if i == 0:
                        result = max(result, startTime[i+1])
                    if i == n - 1:
                        result = max(result, eventTime - endTime[n-2])
                    else:
                        result = max(result, startTime[i+1] - endTime[i-1])
        
        return result


        return result
                

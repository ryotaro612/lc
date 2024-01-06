from collections import defaultdict

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        times = sorted([time for time in set(startTime) | set(endTime)])
        time_map = dict()
        for i, time in enumerate(times):
            time_map[time] = i
        n = len(startTime)
        
        job_map = defaultdict(list)
        for i in range(n):
            job_map[time_map[startTime[i]]].append([time_map[endTime[i]], profit[i]])
        
        time_n = len(time_map)
        dp = [0] * (time_n + 1)

        for time in range(time_n):
            for end, profit in job_map[time]:
                dp[end] = max(dp[end], dp[time] + profit)
            
            dp[time+1] = max(dp[time], dp[time+1])
        return dp[-1]

        

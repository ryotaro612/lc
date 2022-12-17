class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')] * 31

        
        for i, day in enumerate(days):
            if i == 0:
                dp[1] = costs[0]
                dp[7] = costs[1]
                dp[30] = costs[2]
            else:
                next_dp = [float('inf')] * 31
                diff = day - days[i-1]
                for j in range(31):
                    next_dp[max(0, j - diff)] = min(next_dp[max(0, j-diff)], dp[j])
                dp = next_dp
                dp[1] = min(dp[1], dp[0] + costs[0])
                dp[7] = min(dp[7], dp[0] + costs[1])
                dp[30] = min(dp[30], dp[0] + costs[2])
                dp[0] = float('inf')

            # print(day, [(b, d) for b, d in enumerate(dp) if d < float('inf')])
        return min(dp)

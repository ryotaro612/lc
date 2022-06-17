"""
dp[i] num of vacations that I took unitil I reached that city i.
dp[0] = 0
dp[i!=0] = -10000000
dp_prev = dp
dp[i] = max(days[i] + dp_prev[j])
"""
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n_cities = len(flights)
        dp = [-1000000000] * n_cities
        dp[0] = 0
        n_days = len(days[0])
        for day in range(n_days):
            prev = [v for v in dp]
            for city in range(n_cities):
                for start in range(n_cities):
                    if flights[start][city] == 1 or start == city:
                        dp[city] = max(dp[city], prev[start] + days[city][day])

        return max(dp)

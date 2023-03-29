class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        dp = [-float('inf') for _ in range(n+1)]
        dp[0] = 0
        #print(satisfaction)
        for i, s in enumerate(satisfaction):
            next_dp = list(dp)
            # i = 0, j
            for j in range(i+1):
                next_dp[j+1] = max(next_dp[j+1], dp[j] + (j+1) * s)
            dp = next_dp
            #print(dp)
        return max(dp)

"""

"""
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        """
        dp[lap][tire] = min time where i use tire at <lap>
        1000
        
        max 18 consecutive
        """
        tires = list({tuple(tire) for tire in tires})
        dp = [float('inf')] * max(19, numLaps + 1)
        dp[0] = 0
        
        for f, r in tires:
            temp = [0] * 19
            for i in range(1, 19):
                temp[i] = temp[i-1] + f * (r ** (i-1)) 
            for i in range(1, 19):
                dp[i] = min(dp[i], temp[i])
        #print(dp)
        for i in range(numLaps+1):
            for j in range(1, 19):
                if i - j >=0:
                    dp[i] = min(dp[i], dp[i-j] + changeTime + dp[j])
        # print(dp)
        return dp[numLaps]

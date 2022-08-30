"""
[3,4,2]
[2,2,3,3,3,4]
 [1,3,2,3,4,6,6,32,22,2,2,2,1,1,1,1,1,1,1]
"""
from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # ary[i] = (value, n_freq)
        # dp[i] = max(value * n_freq + dp[i+2], dp[i+1])
        # dp[0]
        
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            
        ary = sorted([(k, v) for k, v in count.items()])
        n = len(ary)
        dp = [0] * n
        
        for i in reversed(range(n)):
            base = ary[i][0] * ary[i][1]
            if i + 2 < n:
                if ary[i][0] + 1 == ary[i+1][0]:
                    dp[i] = max(base + dp[i+2], dp[i+1])
                else:
                    dp[i] = base + dp[i+1]
            elif i + 1 < n:
                if ary[i][0] + 1 == ary[i+1][0]:
                    dp[i] = max(base, dp[i+1])
                else:
                    dp[i] = base + dp[i+1]
            else:
                dp[i] = base
        return dp[0]
        # return self.findMax(0, ary, dp)
        

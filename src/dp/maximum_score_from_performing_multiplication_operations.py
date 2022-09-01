    """
[1,2,3]
[3,2,1]

[-5,-3,-3,-2,7,1]
[-10,5,3]

n = len(nums)
dp[i][j] = max(multipliers[j] * nums[i] + dp[i+1][j+1], multipliers[j] * nums[n-1-(j-i)] + dp[i][j+1])
dp[*][m]
"""

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[None] * (m+1) for _ in range(2)]
        
        for num_op in range(m, -1, -1):
            for start in range(num_op, -1, -1):
                if num_op == m:
                    dp[1][start] = 0
                else:
                    dp[1][start] = max(
                        multipliers[num_op] * nums[start] + dp[0][start+1], 
                        multipliers[num_op] * nums[n-1-(num_op-start)] + dp[0][start])
            dp[0], dp[1] = dp[1], dp[0]
        return dp[0][0]
       
    

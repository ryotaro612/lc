from collections import defaultdict
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        """
        n = len(nums)
        dp[i]

        dp[j]  dp[i ] # 0 <= i < j 
        """
        n = len(nums)
        dp = [defaultdict(lambda: 1) for _ in range(n)]
        for j in range(1, n):
            for i in range(j):
                mod = (nums[i] + nums[j]) % k
                dp[j][mod] = max(dp[j][mod], dp[i][mod] + 1)
      
        return max([v for d in dp for v in d.values()])

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        dp = [False] * (total + 1)
        dp[0] = True
        n = len(nums)
        for i in range(n):
            next_dp = list(dp)
            for j in range(len(dp)):
                if dp[j] and j + nums[i] <= total:
                    next_dp[j+nums[i]] = True
            dp = next_dp   
        #for i, v in enumerate(dp):
        #    print(i, v)
        return dp[total // 2]
        

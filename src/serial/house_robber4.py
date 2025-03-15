class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ub = max(nums) + 1
        lb = -1
        while ub - lb > 1:
            mid = (ub + lb) // 2
            
            prev = [0, -float('inf')]

            for i, num in enumerate(nums):
                dp = [0] * 2
                dp[0] = max(prev)

                if mid >= num:
                    dp[1] = prev[0] + 1
                else:
                    dp[1] = -float('inf')
                
                prev = dp

            if max(dp) >= k:
                ub = mid
            else:
                lb  = mid
        
        return ub

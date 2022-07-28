class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        n = len(nums) + 2
        dp = [[None] * n for _ in range(n)]
        
        return self.computeMaxCoins(1, n-1, [1] + nums + [1], dp)
    
    def computeMaxCoins(self, left, right, nums, dp):
        # print(left, right)
        if dp[left][right] is not None:
            return dp[left][right]
        
        result = 0
        for i in range(left, right):
            temp = nums[left-1] * nums[i] * nums[right]
            temp += self.computeMaxCoins(left, i, nums, dp)
            temp += self.computeMaxCoins(i+1, right, nums, dp)
            result = max(temp, result)
        dp[left][right] = result
        return result

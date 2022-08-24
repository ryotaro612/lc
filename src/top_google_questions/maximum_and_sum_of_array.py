"""
[1,3,10,4,7,1]
9

[1,2,3,4,5,6]
3

[1]
1

[1,2,3,4,5,6,1,2,3]
9

[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
9

[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,15,1]
9
"""
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        dp = [dict() for _ in range(n)]
        
        return self.rec(0, 0, dp, nums, numSlots)
        
    def rec(self, nums_i, slot_mask, dp, nums, numSlots):
        n = len(nums)
        if n == nums_i:
            return 0
        
        if slot_mask in dp[nums_i]:
            return dp[nums_i][slot_mask]
        
        result = 0
        for i in range(numSlots*2):
            if not (slot_mask & (1 << i)):
                temp = nums[nums_i] & (i // 2 + 1)
                sub = self.rec(nums_i+1, slot_mask | (1 << i), dp, nums, numSlots)
                temp += sub
                if nums_i < n - 1 and i % 2 == 0 and not (slot_mask & (1<<(i+1))):
                    # print(nums_i, slot_mask, i)
                    dp[nums_i+1][slot_mask | (1 <<(i+1))] = sub
                result = max(result, temp)
        
        dp[nums_i][slot_mask] = result
        return result
        
        
        
        

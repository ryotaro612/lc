class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        result = 1
        cur = nums[0]
        cand = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] < cur:
                result = i + 1
                cur = cand
            else:
                cand = max(cand, nums[i])
        
        return result

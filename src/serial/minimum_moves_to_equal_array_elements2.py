"""
[1,0,0,8,6]
"""
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return min(self.count(nums, nums[max(0, n // 2 - 1)]), self.count(nums, nums[n//2]))
        
    def count(self, nums, target):
        print(target)
        return sum([abs(target - v) for v in nums])

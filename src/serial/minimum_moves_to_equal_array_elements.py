class Solution:
    def minMoves(self, nums: List[int]) -> int:
        least = min(nums)
        res = 0
        for num in nums:
            res += num - least
        return res

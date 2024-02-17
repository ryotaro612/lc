class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            one = len([1 for num in nums if num & (1<<i)])
            result += one * (len(nums) - one)
        return result

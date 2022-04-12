class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = int(n * (n+1) / 2)
        total = sum(nums)
        return expected - total

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([a for a in nums if len(str(a)) % 2 == 0])

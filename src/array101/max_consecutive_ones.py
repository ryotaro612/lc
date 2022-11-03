class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        counter = 0
        for n in nums:
            if n == 0:
                counter = 0
            else:
                counter += 1
                result = max(counter, result)
        return result

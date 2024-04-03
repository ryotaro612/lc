class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        seen = [False] * n
        for num in nums:
            count = 0
            while not seen[num]:
                count += 1
                seen[num] = True
                num = nums[num]
            result = max(result, count)
        return result

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            if nums[abs(nums[i]) - 1] < 0:
                res.append(abs(nums[i]))
            nums[abs(nums[i])-1] *= -1
        return res

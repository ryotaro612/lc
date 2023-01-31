class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        next_nums = [0] * n

        for i in range(n-1, 0, -1):
            for j in range(i+1):
                next_nums[j] = nums[j]
                if j:
                    next_nums[j-1] += nums[j]
                    next_nums[j-1] %= 10
                next_nums[j] %= 10
            temp = nums
            nums = next_nums
            next_nums = temp
            # print(nums)
        return nums[0] 
        

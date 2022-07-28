class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums) # 1 <= ans <= n + 1
        # nums[i] = i + 1 if i + 1 in nums
        # nums[i] != i + 1 otherwise
        for i in range(n):
            num = nums[i]
            while 1<= num <= n:
                temp = nums[num-1]
                if temp == num:
                    break
                else:
                    nums[num-1] = num
                num = temp
        # print(nums)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

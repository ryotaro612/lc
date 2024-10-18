class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        counter = 0
        max_or = 0
        for num in nums:
            max_or = max_or | num
        n = len(nums)
        for i in range(1 << n):
            v = 0
            for j in range(n):
                if i & (1<<j):
                    v |= nums[j]
            if v == max_or:
                counter += 1
        
        return counter

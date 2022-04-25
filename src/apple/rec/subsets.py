class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        result = []
        for i in range(1 << n):
            item = []
            for j in range(n):
                if i & (1 << j):
                    item.append(nums[j])
            result.append(item)
        return result

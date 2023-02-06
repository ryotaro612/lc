"""
[1,2,31,33]
2147483647
"""
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res = 0
        miss = 1
        i = 0

        while miss <= n:
            # print(i, miss, nums[i])
            if i >= len(nums) or nums[i] > miss:
                res += 1
                miss += miss
            elif nums[i] == miss:
                miss += miss
                i += 1
            else:
                miss += nums[i]
                i += 1 
        return res

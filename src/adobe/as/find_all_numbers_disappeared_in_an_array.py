"""
[0,1,2,3,4,5,6,7]
[4,3,2,7,8,2,3,1]

[0,1,2,3,4,5,6,7]
[4,2,3,4,8,2,7,1]

[0,1,2,3,4,5,6,7]
[1,2,3,4,8,2,7,8]

[4 + 1, 5 + 1]
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            if nums[i] == i + 1:
                continue
            temp = nums[i]
            while temp != nums[temp-1]:
                next_temp = nums[temp-1]
                nums[temp-1] = temp
                temp = next_temp
        result = []
        for i in range(n):
            if nums[i] != i + 1:
                result.append(i+1)
        return result

"""
[6,5,5]

[2,2,1,3,1,1,4,1,1,5,1,1,6]
"""
class Solution:
    def majorityElement(self, nums):
        majority = None
        count = 0 
        for num in nums:
            if count == 0:
                majority = num
                count = 1
            elif num == majority:
                count += 1
            else:
                count -= 1
        return majority

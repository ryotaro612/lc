# 12 - sum([1,2,3,4])=10
# sum(nums) - sum([1, 2, 3, ..., n]) 1/2n*(n+1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        rabbit = nums[0]
        turtle = nums[0]
        
        while True:
            turtle = nums[turtle]
            rabbit = nums[nums[rabbit]]
            if turtle == rabbit:
                break
        
        turtle = nums[0]
        while True:
            if turtle == rabbit:
                return turtle
            turtle = nums[turtle]
            rabbit = nums[rabbit]

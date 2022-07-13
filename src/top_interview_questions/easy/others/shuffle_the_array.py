import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums        

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        nums = list(self.nums)    
        result = []
        for _ in range(len(nums)):
            idx =random.randrange(0, len(nums))
            result.append(nums[idx])
            nums[idx] = nums[len(nums) -1]
            nums.pop()
        return result
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

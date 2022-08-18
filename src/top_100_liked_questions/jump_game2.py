"""
        [2,1]
        [1,1,1,1]
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        n  = len(nums)
        n_jumps = 0
        steps = 0
        next_steps = nums[0]
        for i in range(n-1):
            if steps == i:
                n_jumps += 1
                next_steps = max(i+nums[i], next_steps)
                steps = next_steps
            else:
                next_steps = max(i+nums[i], next_steps)
            # print(i, n_jumps, steps, next_steps)
        return n_jumps        

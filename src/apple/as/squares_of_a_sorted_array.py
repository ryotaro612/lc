class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        forward = 0
        for i, v in enumerate(nums):
            if nums[forward] ** 2 > v ** 2:
                forward = i
        
        result = [nums[forward] ** 2]
        forward, backward = forward + 1, forward - 1
        n = len(nums)
        while forward < n or 0 <= backward:
            if forward < n:
                if 0 <= backward:
                    f = nums[forward] ** 2
                    b = nums[backward] ** 2
                    if f <= b:
                        result.append(f)
                        forward += 1
                    else:
                        result.append(b)
                        backward -= 1
                else:
                    result.append(nums[forward] ** 2)
                    forward += 1
            else:
                result.append(nums[backward] ** 2)
                backward -= 1
        return result
                    

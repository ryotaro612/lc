class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        left = n
        for i, num in enumerate(nums):
            while stack and stack[-1][1] > num:
                stack.pop()
                if stack:
                    left = min(left, stack[-1][0]+1)
                else:
                    left = 0
            stack.append([i, num])
        
        stack = []
        right = -1
        for i in range(n-1, -1, -1):
            num = nums[i]

            while stack and stack[-1][1] < num:
                stack.pop()
                if stack:
                    right = max(right, stack[-1][0])
                else:
                    right = n
            stack.append([i, num])
        
        return max(0, right - left)       

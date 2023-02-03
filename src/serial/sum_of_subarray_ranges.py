class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        result = 0
        for right in range(n+1):
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                pivot = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                result -= nums[pivot] * (pivot - left) * (right - pivot)
            stack.append(right)
        stack = []

        for right in range(n+1):
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                pivot = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                result += nums[pivot] * (pivot - left) * (right - pivot)
            stack.append(right)
        return result

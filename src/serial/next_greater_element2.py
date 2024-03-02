class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        results = [-1] * n
        for i in range(n*2):
            while stack and nums[stack[-1]] < nums[i%n]:
                results[stack.pop()] = nums[i%n]
            stack.append(i % n)
        return results

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        left[i] = max(nums[:i+1])
        right[i] = max(nums[i:])
        """
        n = len(nums)
        left = [-float('inf')] * n
        right = [-float('inf')] * n
        left[0] = nums[0]
        for i in range(1, n):
            left[i] = max(left[i-1], nums[i])
        right[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], nums[i])

        result = 0

        for j in range(1, n-1):
            result = max(result, (left[j-1] - nums[j]) * right[j+1])
        
        return result
        

class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        """
        [4]
        [4, 5]
        [4, 5, 5]
        """
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
                continue
            
            if stack[-1] > num:
                continue
            stack.append(num)
        
        return len(stack)

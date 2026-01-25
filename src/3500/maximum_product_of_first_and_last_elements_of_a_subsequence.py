class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        """
        max_pos
        min_pos
        max_neg
        min_neg
        zero = 
        """
        if m == 1:
            result = 0
            for num in nums:
                if result < num * num:
                    result = num * num
            return result

        max_pos = max_neg = -float('inf')
        min_pos = min_neg = float('inf')
        zero = False
        result = -float('inf')

        for i in range(m-1, len(nums)):
            j = i - (m-1)
            if nums[j] > 0:
                max_pos = max(max_pos, nums[j])
                min_pos = min(min_pos, nums[j])
            elif nums[j] == 0:
                zero = True
            else:
                min_neg = min(min_neg, nums[j])
                max_neg = max(max_neg, nums[j])

            for first in [max_pos, min_pos, max_neg, min_neg]:
                if abs(first) < float('inf'):
                    result = max(result, first * nums[i])
            
            if zero:
                result = max(result, 0)
        print(max_pos, min_pos, min_neg, max_neg)
        return result

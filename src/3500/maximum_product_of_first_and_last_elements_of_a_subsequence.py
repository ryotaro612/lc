class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        """

        """
        n = len(nums)
        result = -float('inf')
        for i in range(m-1, len(nums)):
            if i == m-1:
                pos_max = nums[0]
                neg_min = nums[0]
            pos_max = max(pos_max, nums[i-(m-1)])
            neg_min = min(neg_min, nums[i-(m-1)])
            
            result = max(result, nums[i] * pos_max, neg_min * nums[i])
        
        return result

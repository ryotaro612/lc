class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        result = [0] * n 
        left_sum = 0
        right_sum = sum([nums[i] - nums[0] for i in range(1, n)])
        
        """
        i<j <k
        left_sum of j sum(nums[j] - nums[i]) 
        right_sum of j sum(num[k] - nums[j])
        left_sum + nums[j] - nums[j-1]
        right_sum - (nums[j+1] - nums[j])
        """
        for i in range(n):
            result[i] = left_sum + right_sum
            if i < n-1:
                left_sum += (nums[i+1] - nums[i]) * (i+1)
                right_sum -= (nums[i+1] - nums[i]) * (n-i-1)
        return result

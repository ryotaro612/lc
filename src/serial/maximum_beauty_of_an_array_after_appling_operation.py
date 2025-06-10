class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        """
        prefix[i] # of nums[i]
        0<= prefix[i] <= max(nums) + k

        prefix[nums[i]-k] += 1
        prefix[nums[i]+k + 1] -= 1

        prefix[i] += prefix[i-1]

        max(prefix)
        
        """
        n = len(nums)
        maxi = max(nums)
        prefix = [0] * (maxi + k + 2)
        
        for num in nums:
            prefix[max(num-k, 0)] += 1
            prefix[num+k+1] -= 1
        
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
    
        return max(prefix)

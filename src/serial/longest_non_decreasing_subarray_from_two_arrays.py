class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        dp[i][0] dp[i][1]
        nums1[i] num[]
        dp[i+1][0], dp[i+1][1]
        """
        n = len(nums1)
        result = 1
        dp = [[1] * 2 for _ in range(n)]
        for i in range(1, n):
            
            if nums1[i-1] <= nums1[i]:
                dp[i][0] = dp[i-1][0] + 1
            
            if nums2[i-1] <= nums1[i]:
                dp[i][0] = max(dp[i][0], dp[i-1][1] + 1)
            
            if nums2[i-1] <= nums2[i]:
                dp[i][1] = dp[i-1][1] + 1
            
            if nums1[i-1] <= nums2[i]:
                dp[i][1] = max(dp[i][1], dp[i-1][0] + 1)
            
            result = max(result, max(dp[i]))
    
        return result

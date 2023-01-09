class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        dp[i][j] longest subarray of nums1[:i+1] and nums2[:j+1] ends with nums1[i] and nums2[j]
        dp[0][0] = 0
        result max(dp[*][*])
        if nums1[i] == nums[j]
            nums[i+1][j+1]: nums[i][j] + 1
        else:
            nums[i+1][j] = 
        """
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0] * (n2 +1) for _ in range(n1+1)]
        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = 0
        return max([e for ary in dp for e in ary])

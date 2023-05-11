class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 0, 0 = 0
        # 0, 0..2 = 0
        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
                else:
                    dp[i + 1][j + 1] = max(
                        dp[i + 1][j + 1], dp[i][j], dp[i + 1][j], dp[i][j + 1]
                    )

        return dp[n1][n2]


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)

        dp, prev = [0] * (n2 + 1), [0] * (n2 + 1)

        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    dp[j + 1] = prev[j] + 1
                else:
                    dp[j + 1] = max(dp[j], prev[j + 1])
            prev = dp
            dp = [0] * (n2 + 1)
        return prev[n2]

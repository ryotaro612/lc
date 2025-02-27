class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        val_idx = {arr[i]: i for i in range(n)}
        
        for i in range(n):
            for j in range(i+1, n):
                v = arr[i] + arr[j] 
                if v in val_idx:
                    k = val_idx[v]
                    if dp[i][j]:
                        dp[j][k] = max(dp[j][k], dp[i][j] + 1)
                    else:
                        dp[j][k] = max(dp[j][k], 3)

        return max(v for d1 in dp for v in d1)

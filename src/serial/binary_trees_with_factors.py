
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = sorted(arr)
        dp = {v: 1 for v in arr}
        mod = 10**9 + 7
        for i, v in enumerate(arr):
            for j in range(i):
                if v % arr[j] == 0 and v // arr[j] in dp:
                    dp[v] += dp[arr[j]] * dp[v//arr[j]] % mod
                    dp[v] %= mod
        result = 0
        for v in dp.values():
            result += v
            result %= mod
        return result        

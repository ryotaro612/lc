class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[None] * (n+1) for _ in range(n+1)]

        for i in range(n+1):
            for start in range(n-i+1):
                if i <= 1:
                    dp[start][start+i] = True
                elif s[start] == s[start+i-1] and dp[start+1][start+i-1]:
                    dp[start][start+i] = True
                else:
                    dp[start][start+i] = False
        #print(dp)
        cut = [float('inf')] * (n+1)
        cut[0] = 0
        for end in range(n+1):
            if dp[0][end]:
                cut[end] = 0
                continue
            min_cut = end
            for pivot in range(end):
                if dp[pivot][end]:
                    min_cut = min(min_cut, cut[pivot] + 1)
            cut[end] = min_cut
        #print(cut)
        return cut[end]
        

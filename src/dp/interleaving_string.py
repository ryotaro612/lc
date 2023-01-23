"""
"aabcc"
"dbbca"
"aadbbcbcac"

""
""
"a"
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        return self.is_interleave(s1, s2, s3) or self.is_interleave(s2, s1, s3)
    
    def is_interleave(self, s1, s2, s3):
        n1, n2, n3 = [len(s) for s in [s1, s2, s3]]
        dp = [[False] * (n2+2) for _ in range(n1+2)]
        dp[0][0] = True
        for i in range(n1+1):
            for j in range(n2+1):
                if dp[i][j] and n3 > i+j:
                    if i <n1 and s3[i+j] == s1[i]:
                        dp[i+1][j] = True
                    if j <n2 and s3[i+j] == s2[j]:
                        dp[i][j+1] = True
    
        return dp[n1][n2]

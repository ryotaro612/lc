class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        n = len(S)
        m = len(T)
        
        dic = dict()
        for i, s in enumerate(T):
            dic.setdefault(s, []).append(i)
            
        dp = [-1 for i in range(m)]
        
        count = n+1
        start = -1
        
        for index, c in enumerate(S):
            if c in dic:
                for i in dic[c][::-1]:
                    if i == 0:
                        dp[i] = index
                    else:
                        dp[i] = dp[i-1]
                    if i == m-1 and dp[i] >= 0 and index - dp[i]+1 < count:
                        count = index - dp[i] + 1
                        start = dp[i]
        if dp[-1] < 0:
            return ""
        return S[start:start+count]
"""
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n1 = len(s1)
        n2 = len(s2)
        
        dp = [-1] * (n1 + 1)
        
        # dp[i][j] s[dp[i][j]:i]までにs2[:j]が含まれる
        result = None
        for j in range(n2):
            prev = dp
            dp = [-1] * (n1 + 1)
            for i in range(n1):
                if s1[i] == s2[j]:
                    if j == 0:
                        dp[i+1] = i
                    else:
                        dp[i+1] = max(prev[i], dp[i+1])
                    
                else:
                    prev[i+1] = max(prev[i], prev[i+1])
                    dp[i+1] = max(dp[i], dp[i+1])
        
        if dp[n1] == -1:
            return ''
        _, start, end = min([[i - dp[i], dp[i], i] for i in range(n1+1) if dp[i] != -1])
        
        return s1[start:end]
"""

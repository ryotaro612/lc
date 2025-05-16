class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        dp[i] dp[0..i] dp[i+1]
        dp[i]
        """
        n = len(words)
        dp = [[words[i]] for i in range(n)]
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    n_w = len(words[i])
                    if len([k for k in range(n_w) if words[i][k] != words[j][k]]) == 1:
                        if len(dp[i]) < len(dp[j]) + 1:
                            dp[i] = dp[j] + [words[i]]
        
        result = []
        for i in range(n):
            if len(result) < len(dp[i]):
                result = dp[i]
        
        return result

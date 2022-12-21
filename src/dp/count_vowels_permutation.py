class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
        Each vowel 'a' may only be followed by an 'e'.
        Each vowel 'e' may only be followed by an 'a' or an 'i'.
        Each vowel 'i' may not be followed by another 'i'.
        Each vowel 'o' may only be followed by an 'i' or a 'u'.
        Each vowel 'u' may only be followed by an 'a'.
        """
        MOD = 1000000000 + 7
        dp = [1, 1, 1, 1, 1]
            
        for _ in range(n-1):
            next_dp = [0] * 5
            next_dp[1] += dp[0]
            next_dp[1] %= MOD
            
            for i in [0, 2]:
                next_dp[i] += dp[1]
                next_dp[i] %= MOD
            
            for i in range(5):
                if i != 2:
                    next_dp[i] += dp[2]
                    next_dp[i] %= MOD
            
            for i in [2, 4]:
                next_dp[i] += dp[3]
                next_dp[i] %= MOD
            
            next_dp[0] += dp[4]
            next_dp[0] %= MOD
        
            dp = next_dp
        
        result = 0
        for i in range(5):
            result += dp[i]
            result %= MOD
        
        return result

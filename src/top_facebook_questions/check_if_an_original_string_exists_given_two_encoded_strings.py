class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        
        dp  = dict()
        result = self.canBeEquals(0, 0, 0, 0, 'a' + s1 + 'a', 'a' + s2 + 'a', dp)
        # print(dp)
        return result
    def canBeEquals(self, c_pos1, d_pos1, c_pos2, d_pos2, s1, s2, dp):
        key = (c_pos1, d_pos1, c_pos2, d_pos2) 
        if key in dp:
            return dp[key]
        
        n_s1 = len(s1)
        n_s2 = len(s2)
        if c_pos1 == n_s1 - 1 and d_pos1 == 0:
            dp[key] = (c_pos2 == n_s2 - 1 and d_pos2 == 0)
            return dp[key]
        elif c_pos2 == n_s2 - 1 and d_pos2 == 0:
            dp[key] = False
            return dp[key]
        
        if d_pos1 > 0:
            if d_pos2 > 0:
                reduce = min(d_pos1, d_pos2)
                dp[key] = self.canBeEquals(c_pos1, d_pos1 - reduce, c_pos2, d_pos2 - reduce, s1, s2, dp)
                
            else:
                next_pos, patterns = self.enumPatterns(s2, c_pos2 + 1)
                dp[key] = False
                for pattern in patterns:
                    dp[key] = dp[key] or self.canBeEquals(c_pos1, d_pos1-1, next_pos, pattern, s1, s2, dp)
            
        else: # d_pos1 == 0
            if d_pos2 > 0:
                next_pos, patterns = self.enumPatterns(s1, c_pos1 + 1)
                dp[key] = False
                for pattern in patterns:
                    dp[key] = dp[key] or self.canBeEquals(next_pos, pattern, c_pos2, d_pos2 - 1, s1, s2, dp)
            else:
                if s1[c_pos1] != s2[c_pos2]:
                    dp[key] = False
                    return dp[key]
                next_pos1, patterns1 = self.enumPatterns(s1, c_pos1+1)
                next_pos2, patterns2 = self.enumPatterns(s2, c_pos2+1)
                dp[key] = False
                for p1 in patterns1:
                    for p2 in patterns2:
                        dp[key] = dp[key] or self.canBeEquals(next_pos1, p1, next_pos2, p2, s1, s2, dp)
        return dp[key]
                
    def enumPatterns(self, s, pos):
        digits = ''
        #print('start', pos)
        while s[pos].isdigit():
            digits += s[pos]
            pos += 1
        n = len(digits)
    
        if n == 0:
            patterns = [0]
        if n == 1:
            patterns = [int(digits[0])]
        if n == 2:
            patterns = [int(digits[0]) + int(digits[1]), int(digits)]
        if n == 3:
            patterns = [int(digits[0]) + int(digits[1]) + int(digits[2]), int(digits[:2]) + int(digits[2]), int(digits[0]) + int(digits[1:3]), int(digits)]
        #print(s, pos, patterns)
        return pos, patterns

"""
"a"
""

"acbbcda"
"abbdad"
"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        s_n, t_n = len(s), len(t)
        if abs(s_n - t_n) > 1:
            return False
        
        if s_n < t_n:
            t_n, s_n = s_n, t_n
            s, t = t, s
        elif s_n == t_n:
            counter = 0
            for i in range(s_n):
                if s[i] != t[i]:
                    counter += 1
            return counter == 1
            
        i, j = 0, 0
        counter = 0
        # print(s, t)
        while i < s_n and j < t_n:
            if s[i] != t[j]:
                if counter < 1:
                    i += 1
                    counter += 1
                else:
                    return False
            else:
                i += 1
                j += 1
        
        return True

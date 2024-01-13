from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s = [0] * 26
        freq_t = [0] * 26  
        for i in range(len(s)):
            freq_s[ord(s[i]) - ord('a')] += 1
            freq_t[ord(t[i]) - ord('a')] += 1
        
        diff = sum([abs(freq_s[i] - freq_t[i]) for i in range(26)])

        return diff // 2

class Solution:
    def maxScore(self, s: str) -> int:
        left_zeros = 0
        n = len(s)
        score = 0
        num_zeros_in_s = 0
        for c in s:
            if c == '1':
                num_zeros_in_s += 1

        for i in range(n-1):
            if s[i] == '0':
                left_zeros += 1

            score = max(score, left_zeros + (num_zeros_in_s - (i+1 - left_zeros)))
        
        return score

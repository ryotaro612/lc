class Solution:
    def minimumSteps(self, s: str) -> int:
        zero_pos = []
        for i, c in enumerate(s):
            if c == '0':
                zero_pos.append(i)
        
        result = 0
        for i, v in enumerate(zero_pos):
            result += v - i
        return result

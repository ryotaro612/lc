from collections import Counter
class Solution:
    def smallestNumber(self, num: int) -> int:
        s = sorted([c for c in (str(abs(num)))], reverse=num < 0)
        
        pos = next((i for i, c in enumerate(s) if c != '0'), 0)
        s[0], s[pos] = s[pos], s[0]
        s = int(''.join(s))
        if num < 0:
            s *= -1

        return s 

from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        
        n_odd = 0
        for freq in counter.values():
            if freq % 2:
                n_odd += 1
        
        return n_odd <= 1

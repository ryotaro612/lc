from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        if len(s) < k:
            return False
        counter = Counter(s)
        n_odds = 0
        for freq in counter.values():
            if freq % 2:
                n_odds += 1
        
        return True if n_odds <= k else False

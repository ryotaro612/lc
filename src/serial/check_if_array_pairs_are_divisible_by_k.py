from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = defaultdict(int)
        for e in arr:
            if e >= 0:
                counter[e%k] += 1
            else:
                counter[(e%k + k) % k] += 1
        
        if counter[0] % 2:
            return False
        
        for i in counter:
            if i == 0:
                continue
            
            if counter[i] != counter[k-i]:
                return False
        
        return True

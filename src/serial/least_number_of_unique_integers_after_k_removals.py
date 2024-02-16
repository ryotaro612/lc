from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        freq = sorted([f for f in counter.values()], reverse=True)
        while freq and freq[-1] <= k:
            k -= freq[-1]
            freq.pop()
        return len(freq)
            
        

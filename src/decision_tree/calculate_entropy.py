from collections import Counter
import math

class Solution:
    def calculateEntropy(self, input: List[int]) -> float:
        counter = Counter(input)
        
        n = len(input)
        result = 0
        
        for v in counter.values():
            result -= v / n * math.log2(v/n)
        return resultq

import math
from collections import Counter, defaultdict
class Solution:
    def calculateMaxInfoGain(self, petal_length: List[float], species: List[str]) -> float:
        freq = Counter([s for s in species])
        n = len(species)
        h = self.calc(freq)
        
        species = sorted([[l, specie] for l, specie in zip(petal_length, species)])
        species = [s for _, s in species]
        
        left = defaultdict(int)
        result = 0
        print(species, h)
        for i, specie in enumerate(species):
            left[specie] += 1
            freq[specie] -= 1
            temp = h - ((i+1)/n) * self.calc(left) - ((n-i-1)/n)* self.calc(freq)
            
            print(left, freq, temp)
            result = max(result, temp)
        
        return result
    
    def calc(self, freq):
        h = 0
        
        total = sum(freq.values())

        for specie in freq:
            if freq[specie] > 0 and total > 0:
                prob = freq[specie] / total
                h -= prob * math.log(prob,  2)
        return h

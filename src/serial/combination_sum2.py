"""
[8,7,4,3]
11
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        freq = dict()
        for cand in candidates:
            freq[cand] = freq.get(cand, 0) + 1
        freq = [(k, v) for k, v in freq.items()]
        
        return self.findCombis(0, freq, target)[target]
    
    def findCombis(self, pos, freq, target):
        n = len(freq)
          
        result = [[] for _ in range(target+1)]
        if pos == n:
            return result
        
        sub_combis = self.findCombis(pos+1, freq, target)
        cand, count = freq[pos]
        for i in range(1, count+1):
            if cand * i <= target:
                result[cand*i].append([cand] * i)
                
            for j in range(target+1):
                for combi in sub_combis[j]:
                    if cand * i + j <= target:
                        result[cand*i+j].append([cand] * i + combi)
        
        for i in range(target+1):
            result[i].extend(sub_combis[i])
        # print(pos, result)
        return result
        

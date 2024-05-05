class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cache = dict()
        return max([self.find(i, pairs, cache) for i in range(len(pairs))])
    
    def find(self, i, pairs, cache):
        if i in cache:
            return cache[i]
        
        result = 1
        for j in range(len(pairs)):
            if i != j:
                if pairs[j][1] < pairs[i][0]:
                    result = max(result, 1 + self.find(j, pairs, cache))
        
        cache[i] = result
        return result

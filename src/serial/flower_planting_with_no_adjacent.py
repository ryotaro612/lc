class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        result = [-1] * n
        g = [[] for _ in range(n)]
        for a, b in paths:
            g[a-1].append(b-1)
            g[b-1].append(a-1)
        
        for garden in range(n):
            self.traverse(garden, g, result)
        
        return result
    
    def traverse(self, garden, g, result):

        if result[garden] != -1:
            return
        
        cand = {t for t in range(1, 5)}
        for succ in g[garden]:
            if result[succ] in cand:
                cand.remove(result[succ])
        
        result[garden] = list(cand)[0]

        for succ in g[garden]:
            self.traverse(succ, g, result)
        

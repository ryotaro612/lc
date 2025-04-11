
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * n
        for i, a in enumerate(edges):
            scores[a] += i
        
        maxi = max(scores)
        for i in range(n):
            if scores[i] == maxi:
                return i
        

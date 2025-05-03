class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        result = float('inf')
        for v in range(1, 7):
            ok = True
            for i in range(n):
                if tops[i] != v and bottoms[i] != v:
                    ok = False
                    break
            if not ok:
                continue
            
            result = min(result, len([i for i in range(n) if tops[i] != v]))
            result = min(result, len([i for i in range(n) if bottoms[i] != v]))
        
        return result if result < float('inf') else -1

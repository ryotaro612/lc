from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        matrix = [list(r) for r in matrix]
        freq = defaultdict(int)
        
        for r in matrix:
            if r[0]:
                freq[tuple(r)] += 1
            else:
                freq[tuple(0 if c else 1 for c in r)] += 1
        
        return max(freq.values())

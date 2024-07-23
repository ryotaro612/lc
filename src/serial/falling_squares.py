class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        remap = dict()
        
        dots = set()
        for l, width in positions:
            dots.add(l)
            dots.add(l + width)
        
        
        dots = sorted(list(dots))
        idx = 0
        for dot in dots:
            remap[dot] = idx
            idx += 2
        
        n = len(positions)
        heights = []
        for i in range(n):
            heights.append(positions[i][1])
            positions[i] = [remap[positions[i][0]], remap[positions[i][0] + positions[i][1]]]

        vals = [0] * (max(remap.values()) + 1)
        results = []
        # print(positions)
        for i, [l, r] in enumerate(positions):
            
            h = max(vals[l:r+1])
            for j in range(l+1, r):
                vals[j] = h + heights[i]
            results.append(max(vals))
        
        return results
        

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        visit = set()
        direct= [[-1, 0], [0, 1], [1, 0], [0, -1]]
        d_i = 0
        r = rStart
        c = cStart
        while len(result) < rows * cols:
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
            visit.add((r, c))
            # print((r, c))
            if (r + direct[(d_i + 1) % 4][0], c + direct[(d_i + 1) % 4][1]) not in visit:
                d_i = (d_i + 1) % 4
            r += direct[d_i][0]
            c += direct[d_i][1]
            
            
            
        
        return result

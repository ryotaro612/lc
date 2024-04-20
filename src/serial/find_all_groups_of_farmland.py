
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n_rows = len(land)
        n_cols = len(land[0])
        tl = [[None] * n_cols for _ in range(n_rows)]
        br = [[None] * n_cols for _ in range(n_rows)]
        for r in range(n_rows):
            for c in range(n_cols):
                if land[r][c]:
                    if (r == 0 or land[r-1][c] == 0) and (c==0 or land[r][c-1] == 0):
                        tl[r][c] = [r, c]
                    elif r and land[r-1][c]:
                        tl[r][c] = tl[r-1][c]
                    elif c and land[r][c-1]:
                        tl[r][c] = tl[r][c-1]
        
        result = set()
        for r in range(n_rows-1, -1, -1):
            for c in range(n_cols-1, -1, -1):
                if land[r][c]:
                    if (r==n_rows-1 or land[r+1][c] == 0) and (c==n_cols-1 or land[r][c+1] == 0):
                        br[r][c] = [r, c]
                    elif r < n_rows-1 and land[r+1][c]:
                        br[r][c] = br[r+1][c]
                    elif c < n_cols-1 and land[r][c+1]:
                        br[r][c] = br[r][c+1]
        
                    result.add(tuple(tl[r][c] + br[r][c]))
            
        return list(result)
                


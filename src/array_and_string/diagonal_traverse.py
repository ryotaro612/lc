class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n_row = len(mat)
        n_col = len(mat[0])
        result = []
        r, c = 0, 0
        up = True
        while r < n_row and c < n_col:
            result.append(mat[r][c])
                
            if up:
                if r == 0 or c == n_col-1:
                    up = False
                    if c < n_col-1:
                        c += 1
                    else:
                        r += 1
                else:
                    r += -1
                    c += 1
            else:
                if c == 0 or r == n_row - 1:
                    up = True
                    
                    if r < n_row -1:
                        r += 1
                    else:
                        c += 1
                else:
                    r += 1
                    c += -1

        return result
                        
                                

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """
        prefix[i][j] sum of mat[0][0] [i][j]
        """
        n_rows = len(mat)
        n_cols = len(mat[0])
        prefix = [[0] * (n_cols) for _ in range(n_rows)]
        for i in range(n_rows):
            for j in range(n_cols):
                if i:
                    prefix[i][j] += prefix[i-1][j]
                if j:
                    prefix[i][j] += prefix[i][j-1]
                if i and j:
                    prefix[i][j] -= prefix[i-1][j-1]
                
                prefix[i][j] += mat[i][j]
        
        result = 0
        for r in range(n_rows):
            for c in range(n_cols):
                length = max(1, result)
                while 0 <= r-length + 1 and 0 <= c-length + 1:
                    area = prefix[r][c]
                    if 0 < r - length:
                        area -= prefix[r-length][c]
                    if 0 < c - length:
                        area -= prefix[r][c-length]
                    
                    if 0 < r - length and 0 < c-length:
                        area += prefix[r-length][c-length]
                    if area <= threshold:
                        result = max(result, length)

                    length += 1
            
        return result

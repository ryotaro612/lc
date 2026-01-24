class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        """
        """
        n_rows = len(grid)
        n_cols = len(grid[0])
        sum_grid = [[0] * n_cols for _ in range(n_rows)]
        for r in range(n_rows):
            for c in range(n_cols):
                sum_grid[r][c] = grid[r][c]
                if r:
                    sum_grid[r][c] += sum_grid[r-1][c]
                if c:
                    sum_grid[r][c] += sum_grid[r][c-1]
                if r and c:
                    sum_grid[r][c] -= sum_grid[r-1][c-1]
        
        max_k = 1
        for r in range(n_rows):
            for c in range(n_cols):
                 k = max_k + 1
                 while 0 <= r + k -1 < n_rows and 0 <= c + k -1 < n_cols:
                    if self.ok(grid, sum_grid, r, c, k):
                        max_k = max(max_k, k)
                    k += 1
        return max_k
    
    def ok(self, grid, sum_grid, r, c, k):
        total = 0
        for i in range(k):
            total += grid[r+i][c+i]

        for i in range(c, c + k):
            c_sum = sum_grid[r+k-1][i]
            if r:
                c_sum -= sum_grid[r-1][i]
            if i:
                c_sum -= sum_grid[r+k-1][i-1]
            if i and r:
                c_sum += sum_grid[r-1][i-1]
            
            if total != c_sum:
                return False

        for i in range(r, r + k):
            r_sum = sum_grid[i][c+k-1]
            if i:
                r_sum -= sum_grid[i-1][c+k-1]
            if c:
                r_sum -= sum_grid[i][c-1]
            if i and c:
                r_sum += sum_grid[i-1][c-1]
            if total != r_sum:
                return False
        
        rev_diag = 0
        for i in range(k):
            rev_diag += grid[r+i][c+k-1-i]
        
        return rev_diag == total

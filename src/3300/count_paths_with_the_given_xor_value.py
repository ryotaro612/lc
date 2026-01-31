from collections import defaultdict
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        """
        val =        101101
        grid[r][c] = 100101
                     001000 
        """
        n_rows = len(grid)
        n_cols = len(grid[0])
        cache = defaultdict(lambda: dict())

        return self.rec(n_rows-1, n_cols-1, grid, k, cache)

    def rec(self, r, c, grid, k, cache):
        key = (r, c)
        if k in cache[key]:
            return cache[key][k]
        
        if r == 0 and c == 0:
            if k == grid[r][c]:
                cache[key][k] = 1
            else:
                cache[key][k] = 0
            return cache[key][k]
        
        mod = 10**9 + 7
        result = 0
        if r:
            result += self.rec(r-1, c, grid, k ^ grid[r][c], cache)
        if c:
            result += self.rec(r, c-1, grid, k^ grid[r][c], cache)
        cache[key][k] = result % mod
        return cache[key][k]


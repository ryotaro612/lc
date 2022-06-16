"""
3
3
[[0,0],[0,1],[1,2],[2,1]]

1
1
[[0,0]]

2
2
[[0,0],[1,1],[0,1]]


3
3
[[0,0],[0,1],[1,2],[1,2]]
"""
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        result = []
        current = 0
        grid = [[False] * n for _ in range(m)]
        par = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                par[r][c] = (r, c)
        for r, c in positions:
            if grid[r][c]:
                result.append(current)
                continue
            diff = 1
            grid[r][c] = True
            for next_r, next_c in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                if 0 <= next_r and next_r < m and 0<=next_c and next_c < n:
                    if grid[next_r][next_c] and not self.same_group(par, (r, c), (next_r, next_c)):
                        diff -= 1
                        self.unite(par, (r, c), (next_r, next_c))
            current += diff
            result.append(current)
        return result
    
    def find_root(self, par, pos):
        r, c = pos
        if par[r][c] == (r, c):
            return par[r][c]
        
        par[r][c] = self.find_root(par, par[r][c])
        return par[r][c]
    
    def same_group(self, par, pos, pos1):
        return self.find_root(par, pos) == self.find_root(par, pos1)
    
    def unite(self, par, pos, pos2):
        root1 = self.find_root(par, pos)
        root2 = self.find_root(par, pos2)
        par[root1[0]][root1[1]] = root2

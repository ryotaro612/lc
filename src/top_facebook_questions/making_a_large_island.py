"""
[[1,0],[0,1]]
 [[1,1],[1,0]]
"""
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        par = [-1] * (n*n)
        
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                for neigh_r, neigh_c in [(r, c + 1), (r+1, c)]:
                    if neigh_r >= n or neigh_c >= n or grid[neigh_r][neigh_c] == 0:
                        continue
                    self.unite(r * n + c, neigh_r * n + neigh_c, par)
        result = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    result = max(result, self.countSize(r*n+c, par))
                else:
                    roots = set()
                    for neigh_r, neigh_c in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                        if 0<=neigh_r < n and 0 <= neigh_c < n and grid[neigh_r][neigh_c]:
                            roots.add(self.findRoot(neigh_r * n + neigh_c, par)) 
                    count = 1
                    for root in roots:
                        count += self.countSize(root, par)
                    result = max(result, count)
            
        return result
                    
                
        
    def findRoot(self, i, par):
        if par[i] < 0:
            return i
        par[i] = self.findRoot(par[i], par)
        return par[i]
    def isSameGroup(self, a, b, par):
        return self.findRoot(a, par) == self.findRoot(b, par)
    
    def unite(self, a, b, par):
        if self.isSameGroup(a, b, par):
            return
        root_a = self.findRoot(a, par)
        root_b = self.findRoot(b, par)
        
        if par[root_a] < par[root_b]:
            par[root_a] += par[root_b]
            par[root_b] = root_a
        else:
            par[root_b] += par[root_a]
            par[root_a] = root_b
            
    def countSize(self, i, par):
        return -par[self.findRoot(i, par)]
        

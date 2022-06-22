"""
[[1,1,0,0,0],
 [1,1,0,0,0],
 [0,0,0,1,1],
 [0,0,0,1,1]]
[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])
        par = [[-1] * n_col for i in range(n_row)]
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 1:
                    for neigh_r, neigh_c in [cell for cell in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]]:
                        if 0 <= neigh_r and neigh_r < n_row and 0 <= neigh_c and neigh_c < n_col:
                            if grid[neigh_r][neigh_c] == 1:
                                self.unite(par, (i, j), (neigh_r, neigh_c))

        result = 0
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] > 0:
                    result = max(result, self.size(par, (i, j)))
        return result
    
    def find_root(self, par, item):
        if isinstance(par[item[0]][item[1]], int):
            return item
        
        par[item[0]][item[1]] = self.find_root(par, par[item[0]][item[1]])
        return par[item[0]][item[1]]
    
    def is_same_group(self, par, item1, item2):
        return self.find_root(par, item1) == self.find_root(par, item2)
    
    def unite(self, par, item1, item2):
        if self.is_same_group(par, item1, item2):
            return
        
        root1 = self.find_root(par, item1)
        root2 = self.find_root(par, item2)
        if par[root1[0]][root1[1]] < par[root2[0]][root2[1]]:
            par[root1[0]][root1[1]] += par[root2[0]][root2[1]]
            par[root2[0]][root2[1]] = root1
        else:
            par[root2[0]][root2[1]] += par[root1[0]][root1[1]]
            par[root1[0]][root1[1]] = root2
        return
    
    def size(self, par, item):
        root = self.find_root(par, item)
        return -par[root[0]][root[1]]

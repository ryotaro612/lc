class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        par = [[(i, j) for j in range(n)] for i in range(n)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for n_i, n_j in self.get_neighbors(i, j, n):
                    if grid[n_i][n_j] == 1:
                        self.unite(par, (i, j), (n_i, n_j))
        
        islands = dict()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                root = self.find_root(par, (i, j))
                islands.setdefault(root, [])
                for n_i, n_j in self.get_neighbors(i, j, n):
                    if grid[n_i][n_j] == 0:
                        islands[root].append((i, j))
                        break
                        
        # print(islands)
        island1, island2 = islands.values()
        result = float('inf')
        for r1, c1 in island1:
            for r2, c2 in island2:
                result = min(result, abs(r2-r1) + abs(c2-c1))
        return result - 1 
        
    def get_neighbors(self, i, j, n):
        result = []
        for n_i, n_j in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
            if 0 <= n_i and n_i < n and 0 <= n_j and n_j < n:
                result.append((n_i, n_j))
        return result
    
    def find_root(self, par, item):
        i, j = item[0], item[1]
        if item == par[i][j]:
            return item
        par[i][j] = self.find_root(par, par[i][j])
        return par[i][j]
    
    def is_same(self, par, item1, item2):
        return self.find_root(par, item1) == self.find_root(par, item2)
    
    def unite(self, par, item1, item2):
        if self.is_same(par, item1, item2):
            return
        
        root1 = self.find_root(par, item1)
        root2 = self.find_root(par, item2)
        
        par[root1[0]][root1[1]] = root2
        

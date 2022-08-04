class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [-1] * n
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    self.unite(i, j, par)
        
        return len({self.findRoot(i, par) for i in range(n)})
    
    def findRoot(self, i, par):
        if par[i] < 0:
            return i
        else:
            root = self.findRoot(par[i], par)
            par[i] = root
            return root
    def isSameGroup(self, i, j, par):
        return self.findRoot(i, par) == self.findRoot(j, par)
    
    def unite(self, i, j, par):
        if self.isSameGroup(i, j, par):
            return
        
        root_i = self.findRoot(i, par)
        root_j = self.findRoot(j, par)
        
        if par[root_i] < par[root_j]:
            par[root_i] += par[root_j]
            par[root_j] = root_i
        else:
            par[root_j] += par[root_i]
            par[root_i] = root_j
            

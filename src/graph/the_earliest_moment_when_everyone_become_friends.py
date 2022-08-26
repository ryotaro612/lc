"""
[[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]]
4
"""
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        par = [-1] * n
        logs = sorted(logs)
        for timestamp, a, b in logs:
            self.unite(a, b, par)
            if -par[self.findRoot(a, par)] == n:
                return timestamp
        return -1
    
    def findRoot(self, a, par):
        if par[a] < 0:
            return a
        par[a] = self.findRoot(par[a], par)
        return par[a]

    def isSame(self, a, b, par):
        return self.findRoot(a, par) == self.findRoot(b, par)
    
    def unite(self, a, b, par):
        if self.isSame(a, b, par):
            return
        
        root_a = self.findRoot(a, par)
        root_b = self.findRoot(b, par)
        if par[root_a] < par[root_b]:
            par[root_a] += par[root_b]
            par[root_b] = root_a
        else:
            par[root_b] += par[root_a]
            par[root_a] = root_b
    

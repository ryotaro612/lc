class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        
        par = [-1] * n
        
        for i in range(n-1):
            for j in range(i+1, n):
                if self.isSimilar(strs[i], strs[j]):
                    self.unite(i, j, par)
                
        groups = set()
        for i in range(n):
            group = self.findRoot(i, par)
            # print(i, group)
            groups.add(group)
            
        return len(groups)
    
    def isSimilar(self, a: str, b: str):
        if a == b:
            return True
        if len(a) != len(b):
            return False
        
        n = len(a)
        pos = []
        for i in range(n):
            if a[i] != b[i]:
                pos.append(i)
        
        if len(pos) != 2:
            return False
        
        temp = [c for c in a]
        temp[pos[0]], temp[pos[1]] = a[pos[1]], a[pos[0]]
        return ''.join(temp) == b
        
        
    def findRoot(self, i, par):
        if par[i] < 0:
            return i
        par[i] = self.findRoot(par[i], par)
        return par[i]
    
    def isSame(self, a, b, par):
        return self.findRoot(a, par) == self.findRoot(b, par)
    
    def unite(self, a, b, par):
        if self.isSame(a, b, par):
            return True
        
        root_a = self.findRoot(a, par)
        root_b = self.findRoot(b, par)
        
        if par[root_a] < par[root_b]:
            par[root_a] += par[root_b]
            par[root_b] = root_a
        else:
            par[root_b] += par[root_a]
            par[root_a] = root_b

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        par = [-1] * 26

        n  = len(s1)
        for i in range(n):
            a = ord('a')
            self.unite(ord(s1[i]) - a, ord(s2[i]) -a, par)
        
        convert = dict()
        for i in range(26):
            letter = chr(i + ord('a'))
            convert[letter] = letter
            for j in range(i):
                if self.is_same(i, j, par):
                    convert[letter] = chr(j + ord('a'))
                    break
            
        result = []
        for c in baseStr:
            result.append(convert[c])
        
        return ''.join(result)


    def find_root(self, i, par):
        if par[i] < 0:
            return i
        par[i] = self.find_root(par[i], par)
        return par[i]
    
    def is_same(self, a, b, par):
        return self.find_root(a, par) == self.find_root(b, par)
    
    def unite(self, a,b, par):
        if self.is_same(a, b, par):
            return
        
        root_a = self.find_root(a, par)
        root_b = self.find_root(b, par)
        if par[root_a] < par[root_b]:
            par[root_a] += par[root_b]
            par[root_b] = root_a
        
        else:
            par[root_b] += par[root_a]
            par[root_a] = root_b

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        cands = set()
        self.find(s, a, b, cands)

        return min(cands)
    
    def find(self, s, a, b, cands):
        
        lst = [ord(c) - ord('0') for c in s]
        for i in range(1, len(lst), 2):
            lst[i] = (lst[i] + a) % 10
        
        lst_a = ''.join([str(c) for c in lst])
        if lst_a not in cands:
            cands.add(lst_a)
            self.find(lst_a, a, b, cands)
        
        lst_b = list(lst)
        for i in range(len(lst)):
            lst_b[(i + b) % len(lst)] = lst[i]
        
        lst_b = ''.join([str(c) for c in lst_b])

        if lst_b not in cands:
            cands.add(lst_b)
            self.find(lst_b, a, b, cands)

        if lst_b not in cands:
            cands.add(lst_b)
            self.find(lst_b, a, b, cands)
            
